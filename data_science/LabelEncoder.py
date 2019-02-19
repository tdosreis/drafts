import numpy as np
import pandas as pd
from DataWrangling import DataWrangling

class MyLabelEncoder(): 
    '''
    This module is still under development ...
    '''
    
    def __init__(): 
        pass

    def ApplyLabelEncoder(df,string_variables): 
        '''
        Returns a map with all the encoded string variables within a dictionary object
        '''
        from sklearn import preprocessing
        le = preprocessing.LabelEncoder()

        AllMaps = {}
        for i in string_variables:
            le.fit(df[str(i)])
            AllMaps[str(i)] = dict(zip(le.classes_, le.transform(le.classes_)))

        return AllMaps

    def LabelEncodeDict(data_dictionary,variables,mapping_dictionary,inplace=False): 
        '''
        Applies encoder to each string variable in a dictionary
        '''
        data = DataWrangling.GetSubDictionary(data_dictionary,variables)

        for var in variables: 
            data[str(var)] = pd.Series([mapping_dictionary[str(var)].get(x) for x in data[str(var)]])

        if not inplace: 
            return data

        else: 
            for var in variables: 
                data_dictionary[var] = data[var]