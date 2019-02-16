import numpy as np
import pandas as pd

class DataWrangling(): 
    '''
    A collection of various data manipulation tools
    
    Author: Tiago Rosa dos Reis
    '''
    def __init__(self): 
        self.values = data
        
    def ConvertToArray(data): 
        return np.asarray(data)

    def CheckString(data): 
        return [isinstance(x, str) for x in data]

    def GetStrings(data): 
        mask = CheckString(data)
        values = ConvertToArray(data)
        return values[mask].tolist()

    def InvertBool(data): 
        return [not i for i in data]

    def ConvertStrToFloat(data): 
        return [float(i) for i in data]
    
    def PercentageOfNaN(data): 
        return round(float(data.isna().sum())/data.shape[0],2)

    def CheckString(data):
        return list(map(lambda x: isinstance(x, str), data))

    def InvertBool(data): 
        return list(map(lambda x: not(x), data))

    def ConvertStrToFloat(data): 
        return list(map(lambda x: float(x), data))

    def RemoveStrings(data): 
        mask = CheckString(data)
        inverse_mask = InvertBool(mask)
        values = ConvertToArray(data)
        filtered_data = values[inverse_mask]
        return ConvertStrToFloat(filtered_data)
        
    def EnumerateList(values): 
        '''
        Introduces an index to a list of values
        '''
        return [(i,j) for (i,j) in enumerate(values)]
    
    def ConvertDataframeToDict(data):
        '''
        Converts a given dataframe into a dictionary
        '''
        return {i:data[i] for i in data.columns.values}

    def ConvertListsToTuples(values):
        '''
        Converts a list of lists to a list of dictionaries
        '''
        return [tuple(values[i]) for i in range(len(values))]

    def ConvertTuplestoDicts(values,col_index=0,p0=1,pN=False):
        '''
        Converts a list of tuples to a list of dictionaries
        '''
        if pN is False:        
            return {item[col_index]: item[p0] for item in values}
        else: 
            return {item[col_index]: item[p0:pN] for item in values}

    def MatchDictionaryWithDataframe(values,items_dict,matching_column):
        '''
        Match a list of dictionaries to corresponding values on a dataframe
        '''
        trans = values.apply(lambda x: None if str(x) == 'nan' else items_dict.get(x)[matching_column])   

        return trans

    def BinsToLabels(bins_list):
        '''
        Converts a list of bins to corresponding intervals as string
        '''
        labels = []
        for i in range(len(bins_list) - 1):
            string = str(bins_list[i]) + ' - ' + str(bins_list[i+1])
            labels.append(string)

        return labels
    
    def ComputeRowsColumns(nRows,nCols):
        '''
        Computes all nRows,nCols combinations and with indexation
        '''
        index = [[i,j] for i in range(nRows) for j in range(nCols)]
        [index[i].insert(0,i) for i,j in enumerate(index)][0]
        return index

    def ConvertMultiEntryToDict(multEntryTuples, repeatedIndex, referenceList):
        '''
        Matches a list of multiple repeated entries to a reference list of single values
        '''
        j = 0
        vals = []
        d = {}
        for i in range(len(multEntryTuples) - 1):
            if multEntryTuples[i+1][repeatedIndex] == referenceList[j]:
                vals.append(multEntryTuples[i][1:])
                d[referenceList[j]] = vals
            else:
                vals = []
                j+=1

        return d

    def ComputeAllLists(data,nCols=3):
        '''
        Computes a summarized list with all the variables, indices and plotting positions for a general plotting function
        '''
        varsList = list(data.columns.values)
        import math
        nRows = math.ceil(len(varsList)/3)
        remove = len(DataWrangling.ComputeRowsColumns(nRows,nCols)) - len(varsList)

        if remove != 0: 
            ref_   = DataWrangling.ComputeRowsColumns(nRows,nCols)[:-remove]
        elif remove == 0: 
            ref_ = DataWrangling.ComputeRowsColumns(nRows,nCols)

        [ref_[i].insert(0,varsList[i]) for i in range(len(varsList))][0]
        
        return ref_,varsList
    
class Operations():
    '''
    A class of various statistical functions.
    
    Any function can be added to this Python script and its output will be computed in 'SummarizeData'.
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
    def main(): 
        '''
        Put code here ...
        '''
        
    print('DataWrangling running as main script')
    
else:
    print('DataWrangling imported from another module')