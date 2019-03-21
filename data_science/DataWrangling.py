import numpy as np
import pandas as pd

class DataWrangling(): 
    """
    A collection of various tools for data manipulation
    
    Author: Tiago Rosa dos Reis
    """
    def __init__(self): 
        pass
        
    def ConvertToArray(self,data,dtype=object): 
        '''
        Converts a list to a NumPy array
        '''
        return np.asarray(self,data,dtype=dtype)
    
    def FlatList(self,data): 
        '''
        Flattens a list of lists
        '''
        return [item for sublist in data for item in sublist]
    
    def ConvertDataType(self,data,dtype=float): 
        '''
        Converts a list of (string) values to a specific data type (str, float, int)
        '''
        return list(map(lambda x: dtype(x), data))

    def CheckDataType(self,data,dtype=str):
        '''
        Check if each element in a list of values belongs to a certain data type
        '''
        return list(map(lambda x: isinstance(x, dtype), data))
    
    def InvertBool(self,data): 
        '''
        Returns the opposite in a True or False list
        '''
        return list(map(lambda x: not(x), data))

    def GetDataType(self,data,dtype=str,reverse=False): 
        '''
        Returns a list with the data types of each element in a list
        '''
        data = ConvertToArray(data)
        mask = CheckDataType(data,dtype=dtype)
        
        mask = np.where(reverse,InvertBool(mask),mask)

        return data[mask]

    def PercentageMissing(self,data,precision=2): 
        '''
        Returns the percentage of missing values in a pandas Series
        '''
        return round(float(data.isnull().sum())/data.shape[0],precision)
        
    def EnumerateList(self,data): 
        '''
        Introduces an index to a list of values
        '''
        return [(i,j) for (i,j) in enumerate(data)]
    
    def ConvertDataToDict(self,data):
        '''
        Converts a given dataframe into a dictionary
        '''
        return {i:data[i] for i in data.columns.values}
    
    def GetSubDictionary(self,dictionary,variables): 
        '''
        Returns a sub-dictionary from a dictionary
        '''
        return {var: dictionary[var] for var in variables if var in dictionary}

    def ConvertListsToTuples(self,data):
        '''
        Converts a list of lists to a list of tuples
        '''
        return [tuple(data[i]) for i in range(len(data))]

    def ConvertTuplestoDicts(self,data,col_index=0,p0=1,pN=False):
        '''
        Converts a list of tuples to a list of dictionaries
        '''       
        if not pN:        
            return {item[col_index]: item[p0] for item in data}
        else: 
            return {item[col_index]: item[p0:pN] for item in data}

    def MatchDictWithData(self,data,items_dict,matching_column):
        '''
        Match a list of dictionaries to corresponding values on a dataframe
        '''
        return data.apply(lambda x: None if str(x) == 'nan' else items_dict.get(x)[matching_column])   

    def BinsToLabels(self,bins_list):
        '''
        Converts a list of bins to corresponding intervals as a string
        '''
        labels = [str(bins_list[i]) + ' - ' + str(bins_list[i+1]) for i in range(len(bins_list) - 1)]

        return labels
    
    def ComputeRowsColumns(self,nRows,nCols):
        '''
        Computes all nRows,nCols combinations with indexation
        '''
        index = [[i,j] for i in range(nRows) for j in range(nCols)]

        for i,j in enumerate(index): 
            index[i].insert(0,i)

        return index

    def ReplaceMissing(self,v,replacer=None):
        '''
        Replaces all missing values in a list
        '''
        v    = np.asarray(v)
        mask = np.isnan(v)

        TrueVals  = v[ ~ mask]
        FalseVals = [replacer]*len(v[mask])

        selector = [iter(TrueVals), iter(FalseVals)]
        results  = [next(selector[i]) for i in mask]

        return results
    
    def FrequencyCounter(self,values,list_index=True):
        '''
        Computes the absolute frequency of items on a dataframe
        '''
        values = sorted([[i,j] for [i,j] in zip(values,values.index) if str(i) != 'nan'])

        if list_index:
            for i,j in enumerate(values):
                values[i].insert(0,i)
        else:
            pass

        return values
    
    def CumulativePercentage(self,values,col_index=1):
        '''
        Computes the cumulative percentage of values in a list
        '''
        from itertools import groupby

        vals    = [i[col_index] for i in values]
        unique  = sorted(list(set(vals)))
        freq    = [len(list(group)) for key, group in groupby(vals)]

        cum_pct = np.cumsum(freq)/len(values)
        summary = [(i,j,k) for (i,j,k) in zip(unique, freq, cum_pct)]

        return summary

    def ConvertMultiEntryToDict(self,multEntryTuples, repeatedIndex, referenceList):
        '''
        Matches a list of multiple repeated entries to a reference list of single values
        '''
        j = 0
        vals, d = [], {}

        for i in range(len(multEntryTuples) - 1):
            if multEntryTuples[i+1][repeatedIndex] == referenceList[j]:
                vals.append(multEntryTuples[i][1:])
                d[referenceList[j]] = vals
            else:
                vals = []
                j+=1
                
        return d
    
class Operations():
    '''
    A class of various statistical functions.
    
    Any function can be added to this Python script and its output 
    will be computed in 'SummarizeData' (see DataAnalysis.py script).
    '''
    def __init__(self,data): 
        self.values = data
    
    def CountNan(self):
        '''
        Returns the quantity of missing values
        '''
        return np.isnan(self.values).sum()

    def EvalType(self):
        '''
        Python's 'dtype'
        '''
        return self.values.dtype.name

    def CountUnique(self):
        '''
        Returns the quantity of unique values
        '''
        return self.values.nunique()

    def CountTotal(self):
        '''
        Returns the total quantity of values
        '''
        return self.values.shape[0]

    def PctNan(self):
        '''
        Returns the percentage of missing values
        '''
        return self.CountNan()/self.CountTotal()   
    
    def MeanValue(self): 
        '''
        Returns the mean value of a data series
        '''
        return self.values.mean()
    
    def MedianValue(self): 
        '''
        Returns the median value of a data series
        '''
        return self.values.median()
    
    def MaxValue(self): 
        '''
        Returns the mean value of a data series
        '''
        return self.values.max()
    
    def MinValue(self):
        '''
        Returns the minimum value of a data series
        '''
        return self.values.min()
    
    def Variance(self): 
        '''
        Returns the variance within a data series
        '''
        return self.values.var()
    
    def Summation(self): 
        '''
        Returns the summation of values within a data series
        '''
        return self.values.sum()
    
    def StandardDeviation(self):
        '''
        Returns the standard deviation of a numeric variable
        '''
        return self.values.std()
    
if __name__ == '__main__': 

    main = DataWrangling
    
    print('Data Analysis running as main script')
    
else:
    print('Data Analysis imported from another module')