import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import Imputer
from statsmodels.stats.outliers_influence import variance_inflation_factor

class ReduceVIF(BaseEstimator, TransformerMixin):
    '''
    Computes the VIF stepwise selection regression
    '''
    def __init__(self, thresh=5.0, impute=True, impute_strategy='median'):
        self.thresh = thresh
        if impute:
            self.imputer = Imputer(strategy=impute_strategy)

    def fit(self, X, y=None):
        print('ReduceVIF fit')
        if hasattr(self, 'imputer'):
            self.imputer.fit(X)
        return self

    def transform(self, X, y=None):
        print('ReduceVIF transform')
        columns = X.columns.tolist()
        if hasattr(self, 'imputer'):
            X = pd.DataFrame(self.imputer.transform(X), columns=columns)
        return ReduceVIF.calculate_vif(X, self.thresh)

    @staticmethod
    def calculate_vif(X, thresh=5.0):
        # Taken from https://stats.stackexchange.com/a/253620/53565 and modified
        dropped=True
        while dropped:
            variables = X.columns
            dropped = False
            vif = [variance_inflation_factor(X[variables].values, X.columns.get_loc(var)) for var in X.columns]
            
            max_vif = max(vif)
            if max_vif > thresh:
                maxloc = vif.index(max_vif)
                print(f'Dropping {X.columns[maxloc]} with vif={max_vif}')
                X = X.drop([X.columns.tolist()[maxloc]], axis=1)
                dropped=True
        return X
    
    
# import packages
import pandas as pd
import numpy as np
import pandas.core.algorithms as algos
from pandas import Series
import scipy.stats.stats as stats
import re
import traceback
import string

class ComputeIV(): 
    '''
    Computes the Information Value (IV) for a specific dataset
    '''
    def __init__(self,max_bin,force_bin): 
        self.max_bin = max_bin
        self.force_bin = force_bin

    # define a binning function
    def mono_bin(self, Y, X,):
        
        n = self.max_bin

        df1 = pd.DataFrame({"X": X, "Y": Y})
        justmiss = df1[['X','Y']][df1.X.isnull()]
        notmiss = df1[['X','Y']][df1.X.notnull()]
        r = 0
        while np.abs(r) < 1:
            try:
                d1 = pd.DataFrame({"X": notmiss.X, "Y": notmiss.Y, "Bucket": pd.qcut(notmiss.X, n)})
                d2 = d1.groupby('Bucket', as_index=True)
                r, p = stats.spearmanr(d2.mean().X, d2.mean().Y)
                n = n - 1 
            except Exception as e:
                n = n - 1

        if len(d2) == 1:
            n = self.force_bin         
            bins = algos.quantile(notmiss.X, np.linspace(0, 1, n))
            if len(np.unique(bins)) == 2:
                bins = np.insert(bins, 0, 1)
                bins[1] = bins[1]-(bins[1]/2)
            d1 = pd.DataFrame({"X": notmiss.X, "Y": notmiss.Y, "Bucket": pd.cut(notmiss.X, np.unique(bins),include_lowest=True)}) 
            d2 = d1.groupby('Bucket', as_index=True)

        d3 = pd.DataFrame({},index=[])
        d3["MIN_VALUE"] = d2.min().X
        d3["MAX_VALUE"] = d2.max().X
        d3["COUNT"] = d2.count().Y
        d3["EVENT"] = d2.sum().Y
        d3["NONEVENT"] = d2.count().Y - d2.sum().Y
        d3=d3.reset_index(drop=True)

        if len(justmiss.index) > 0:
            d4 = pd.DataFrame({'MIN_VALUE':np.nan},index=[0])
            d4["MAX_VALUE"] = np.nan
            d4["COUNT"] = justmiss.count().Y
            d4["EVENT"] = justmiss.sum().Y
            d4["NONEVENT"] = justmiss.count().Y - justmiss.sum().Y
            d3 = d3.append(d4,ignore_index=True)

        d3["EVENT_RATE"] = d3.EVENT/d3.COUNT
        d3["NON_EVENT_RATE"] = d3.NONEVENT/d3.COUNT
        d3["DIST_EVENT"] = d3.EVENT/d3.sum().EVENT
        d3["DIST_NON_EVENT"] = d3.NONEVENT/d3.sum().NONEVENT
        d3["WOE"] = np.log(d3.DIST_EVENT/d3.DIST_NON_EVENT)
        d3["IV"] = (d3.DIST_EVENT-d3.DIST_NON_EVENT)*np.log(d3.DIST_EVENT/d3.DIST_NON_EVENT)
        d3["VAR_NAME"] = "VAR"
        d3 = d3[['VAR_NAME','MIN_VALUE', 'MAX_VALUE', 'COUNT', 'EVENT', 'EVENT_RATE', 'NONEVENT', 'NON_EVENT_RATE', 'DIST_EVENT','DIST_NON_EVENT','WOE', 'IV']]       
        d3 = d3.replace([np.inf, -np.inf], 0)
        d3.IV = d3.IV.sum()

        return(d3)

    def char_bin(self,Y, X):

        df1 = pd.DataFrame({"X": X, "Y": Y})
        justmiss = df1[['X','Y']][df1.X.isnull()]
        notmiss = df1[['X','Y']][df1.X.notnull()]    
        df2 = notmiss.groupby('X',as_index=True)

        d3 = pd.DataFrame({},index=[])
        d3["COUNT"] = df2.count().Y
        d3["MIN_VALUE"] = df2.sum().Y.index
        d3["MAX_VALUE"] = d3["MIN_VALUE"]
        d3["EVENT"] = df2.sum().Y
        d3["NONEVENT"] = df2.count().Y - df2.sum().Y

        if len(justmiss.index) > 0:
            d4 = pd.DataFrame({'MIN_VALUE':np.nan},index=[0])
            d4["MAX_VALUE"] = np.nan
            d4["COUNT"] = justmiss.count().Y
            d4["EVENT"] = justmiss.sum().Y
            d4["NONEVENT"] = justmiss.count().Y - justmiss.sum().Y
            d3 = d3.append(d4,ignore_index=True)

        d3["EVENT_RATE"] = d3.EVENT/d3.COUNT
        d3["NON_EVENT_RATE"] = d3.NONEVENT/d3.COUNT
        d3["DIST_EVENT"] = d3.EVENT/d3.sum().EVENT
        d3["DIST_NON_EVENT"] = d3.NONEVENT/d3.sum().NONEVENT
        d3["WOE"] = np.log(d3.DIST_EVENT/d3.DIST_NON_EVENT)
        d3["IV"] = (d3.DIST_EVENT-d3.DIST_NON_EVENT)*np.log(d3.DIST_EVENT/d3.DIST_NON_EVENT)
        d3["VAR_NAME"] = "VAR"
        d3 = d3[['VAR_NAME','MIN_VALUE', 'MAX_VALUE', 'COUNT', 'EVENT', 'EVENT_RATE', 'NONEVENT', 'NON_EVENT_RATE', 'DIST_EVENT','DIST_NON_EVENT','WOE', 'IV']]      
        d3 = d3.replace([np.inf, -np.inf], 0)
        d3.IV = d3.IV.sum()
        d3 = d3.reset_index(drop=True)

        return(d3)

    def data_vars(self,df1, target):

        stack = traceback.extract_stack()
        filename, lineno, function_name, code = stack[-2]
        vars_name = re.compile(r'\((.*?)\).*$').search(code).groups()[0]
        final = (re.findall(r"[\w']+", vars_name))[-1]

        x = df1.dtypes.index
        count = -1

        for i in x:
            if i.upper() not in (final.upper()):
                if np.issubdtype(df1[i], np.number) and len(Series.unique(df1[i])) > 2:
                    conv = self.mono_bin(target, df1[i])
                    conv["VAR_NAME"] = i
                    count = count + 1
                else:
                    conv = self.char_bin(target, df1[i])
                    conv["VAR_NAME"] = i            
                    count = count + 1

                if count == 0:
                    iv_df = conv
                else:
                    iv_df = iv_df.append(conv,ignore_index=True)

        iv = pd.DataFrame({'IV':iv_df.groupby('VAR_NAME').IV.max()})
        iv = iv.reset_index()
        return iv