import pandas as pd
import numpy as np
from DataWrangling import DataWrangling, Operations

class PreAnalysis():
    """
    Analyzes any dataframe and computes multiple types of statistics, information and post-processing information
    
    author: Tiago Rosa dos Reis
    """
    def __init__(self,data):
        
        self.dataset = data
        self.variables = data.columns.values
        self.description = data.describe(include='all')
        self.categories = {}
        self.info = {}
        self.binaries = {}
        
    def ReadMe(self,):
        '''
        Displays all the functions within PreAnalysis' module
        '''
        print('>>> read_me(), binary(), types(), plot_missing(), missing()')
        
    def ToDateTime(self,variable):
        '''
        Converts a variable to datetime format
        '''
        self.dataset[str(variable)] = pd.to_datetime(self.dataset[str(variable)])
        
    def CheckBinaries(self,):
        """
        Identifies all binary variables (possible 'targets' for predictive modeling)
        """
        self.binaries['nUnique < 2'] = [i for i in self.variables if self.dataset[i].nunique() <  2]
        self.binaries['nUnique = 2'] = [i for i in self.variables if self.dataset[i].nunique() == 2]
        self.binaries['nUnique > 2'] = [i for i in self.variables if self.dataset[i].nunique() >  2]
                       
        return self.binaries
                    
    def dTypes(self,):
        """
        Groups pandas data types
        """
        dataTypes = list(set([self.dataset.dtypes[i].name for i in range(len(self.dataset.columns.values))]))
        
        for j in dataTypes:
            self.categories[str(j)] = [i for i in self.variables if self.dataset[i].dtypes == j]
          
        return self.categories
    
    def CountNaN(self,):
        '''
        Counts the number of missing values per variable
        '''
        nanTuples = sorted([(self.dataset[i].isna().sum(),i) for i in self.dataset.columns.values],reverse=True)
        nanDicts = DataWrangling.ConvertTuplestoDicts(nanTuples,1,0)    
        return(nanDicts)
  
    def PlotMissing(self,variables):
        '''
        Displays a grafic image of all the missing values of each variable
        '''
        import seaborn as sns
        import matplotlib.pyplot as plt
        
        print('Missing values appear as yellow lines')
        
        plt.figure(figsize=(16,4))
        return sns.heatmap(self.dataset[variables].isnull(),cmap='viridis')    
    
    def MissingStats(self,):
        '''
        Displays all information about missing values
        '''
        missing    = [i for i in self.variables if     np.any(self.dataset[i].isnull())]
        notMissing = [i for i in self.variables if not np.any(self.dataset[i].isnull())]
        
        print('Total number of variables: ', len(self.variables), '\n')
     
        if len(missing) == 0:
            print('All variables are fulfilled!')
        else:
            print('Number of variables with at least one missing value: ', len(missing), '====>>>>>', missing, '\n')
        
        def AllNumerical(data): 
            return all(isinstance(x, (int,float)) for x in data)
        
        standardDev = self.dataset.apply(lambda x: x.std() if AllNumerical(x) is True else np.nan)
        numLines    = self.dataset.apply(lambda x: x.count(), axis=0)
        
        List1 = self.variables[(standardDev == 0) & (numLines == self.dataset.shape[0])]
        List2 = self.variables[(standardDev == 0) & (numLines != self.dataset.shape[0])]
        List3 = self.variables[(standardDev.isnull())]
        List4 = self.variables[(standardDev != 0) & ( ~ standardDev.isnull())]
                            
        print('Number of variables per criterion of analysis: ','\n')
        print('std = 0 and not NaN: ',    List1)
        print('std = 0 and NaN: ',        List2)
        print('std = NaN, other cases: ', List3)
        print('other variables: ',        List4, '\n')
        print('number of fulfilled variables: ', len(notMissing), ' >>>', notMissing, '\n')

        self.info['std == 0.0 (type 1)'] = List1
        self.info['std == 0.0 (type 2)'] = List2
        self.info['std == NaN']     = List3

        return self.info

class SummarizeData():
    '''
    Outputs a dataframe with different statistical information for a given set of values
    '''
    def __init__(self,data,):
        
        self.variables   = data.columns.values
        self.dataset     = data
        self.Operations  = Operations
        
    def AllFunctions(self,): 
        '''
        List of all statistical functions within Operations module
        '''
        return [func for func in dir(self.Operations) if callable(getattr(self.Operations, func)) and not func.startswith("__")] 
    
    def ComputeAllFunctions(self,): 
        '''
        Displays a dictionary with all the calculated functions
        '''
        funcs = self.AllFunctions()
        d = {variable: [getattr(self.Operations(self.dataset[str(variable)]), func)() for func in funcs] for variable in self.variables}
        return d
    
    def DataStats(self,):
        '''
        Displays a dataframe with statistical information about a dataset
        '''
        from DataWrangling import DataWrangling
        data = pd.DataFrame(self.ComputeAllFunctions())
        newColumns = DataWrangling.ConvertTuplestoDicts(DataWrangling.EnumerateList(self.AllFunctions()),0)
        return data.transpose().rename(columns=newColumns).reset_index().rename(columns={'index':'Variable'})       
        
if __name__ == '__main__': 
    
    def Summary(): 
        return SummarizeData(df,)

    main = Summary()
    
    print('Data Analysis running as main script')
    
else:
    print('Data Analysis imported from another module')