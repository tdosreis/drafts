from collections import Counter
from DataWrangling import DataWrangling
from DataBinning import *
import numpy as np
import pandas as pd
import seaborn as sns

def SplitData(data,n_partitions=8,axis=1): 
    return np.array_split(data,n_partitions,axis)

def SplitArgs(args,column_wise=True,n_partitions=8):
    
    """
    Generalized approach for preparing the 
    arguments of a multiple-argument function in
    parallel processing tasks
    
    Inputs
    ======
    args: format should be a list
    list(data,*args)
    first value of the list is the data to be split
    
    if column_wise = False, then "row_wise" split is applied (this includes other data-type arguments in the list)
    
    Data values must be either a pandas dataframe or a pandas Series
    """
    
    X = args[0]
    
    # column-wise argument parallelism
    if column_wise: 
        splits = SplitData(X,n_partitions,axis=1) 
        args_  = [[X_, args[1:]] for (_, X_) in enumerate(splits)]
        
        for index, items in enumerate(args_): # flat mixed types list
            args_[index] = [y for x in items for y in (x if isinstance(x, list) else (x,))]
        
        return args_
        
    # row-wise argument parallelism    
    elif not column_wise: 
        args_ = []
        for index, element in enumerate(args): 
            if isinstance(element,pd.core.series.Series) or isinstance(element,pd.core.frame.DataFrame): 
                args_.append(SplitData(element,n_partitions,axis=0))
            else:
                args_.append(element)
            
        return args_    

from collections import Counter
import numpy as np
import pandas as pd
import seaborn as sns

def ComputeProbs(data,compute_nan=False):
    '''
    Computes the probability mass function of a list of values
    '''
    if type(data) is np.ndarray: 
        data = data.tolist()
    else:
        pass
        
    N = np.where(compute_nan is False, np.sum( ~ np.isnan(data)), len(data))
    P = [(i,float(j)/N) for (i,j) in Counter(data).items()]
    P = DataWrangling().ConvertTuplestoDicts(P,0,1)
    
    if not compute_nan and np.nan in P.keys(): 
        P.pop(np.nan)
    else: 
        pass
    
    return P

def ElementWiseProbs(data,compute_nan=False,items_set=False): 
    '''
    Computes the probability of each element in a list of values
    '''
    P = ComputeProbs(data,compute_nan=compute_nan)
    
    if not items_set: 
        return list(map(lambda x: P.get(x),data))
    else: 
        return list(P.values())
    
def ShannonEntropy(data,bins,compute_nan=False,compute_bins=True):
    '''
    Computes the discrete Shannon's entropy H(X) for a list of values (X)
    '''
    if compute_bins: 
        x = DataBinning(data).ConvertData(bins,show_boundaries=False)
    else: 
        x = np.array(data)
    
    probs = ElementWiseProbs(x,compute_nan=compute_nan,items_set=True)

    return -sum(list(map(lambda p: p*np.log(p), filter(None,probs))))

def DistributionPlot(vals,X,Y,x_bins,y_bins,figSize=(10,6)): 
    '''
    Plots a seaborn heatmap for binned variables X and Y
    '''
    fig, ax = plt.subplots(1,1,figsize=figSize)
    
    sns.heatmap(vals,
                cmap = 'Blues',
                ax=ax,annot=True,fmt='.3f',
                annot_kws = {'fontsize':10,'weight':'bold'},
                yticklabels = DataBinning(vals).LabelBins(X,x_bins),
                xticklabels = DataBinning(vals).LabelBins(Y,y_bins))
    
    ax.tick_params(labelsize = 12,labelcolor='black')

def JointProbability(X,Y,x_bins,y_bins,compute_probs=True,plot_graph=False): 
    '''
    Joint probability between X and Y variables
    '''    
    quants = np.histogram2d(X,Y,[x_bins,y_bins])[0]
    
    probs = quants/np.sum(quants)
    
    vals = np.where(compute_probs, probs, quants)
    
    if not plot_graph: 
        pass
    else: 
        DistributionPlot(vals,X,Y,x_bins,y_bins)

    return vals   
    
def JointEntropy(X,Y,x_bins,y_bins):
    '''
    Computs the joint entropy between X and Y variables
    '''
    probs = JointProbability(X,Y,x_bins,y_bins,compute_probs=True).ravel()

    return - (np.nansum(probs*np.log(probs)))

def MutualInformation(X,Y,x_bins,y_bins,normalized=True): 
    '''
    Computes the mutual information between X and Y variables
    '''
    MI = ShannonEntropy(X,x_bins) + ShannonEntropy(Y,y_bins) - JointEntropy(X,Y,x_bins,y_bins)
    
    if normalized: 
        return round(MI / ShannonEntropy(Y,y_bins),4)
    else:
        return round(MI,4)

def FeatureSelection(df,target,x_bins,target_bins,method='mutual_information',normalized=True): 
    '''
    Display a ranking of the most significant variables in a dataset
    '''
    if method == 'mutual_information': 
        variables = df.columns.values
        return sorted([(MutualInformation(df[str(variable)],target,x_bins,target_bins,normalized=normalized), \
                        variable) for variable in variables],reverse=True)



