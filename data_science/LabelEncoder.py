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

def ConvertDataframeToDict(data):
    '''
    Converts a given dataframe into a dictionary
    '''
    return {i:data[i] for i in data.columns.values}

def GetSubDictionary(dictionary,variables): 
    '''
    Returns a sub-dictionary
    '''
    return {var: dictionary[var] for var in variables if var in dictionary}

def LabelEncodeDict(data_dictionary,variables,mapping_dictionary,inplace=False): 
    '''
    Applies encoder to each string variable in a dictionary
    '''
    data = GetSubDictionary(data_dictionary,variables)
    
    for var in variables: 
        data[str(var)] = pd.Series([mapping_dictionary[str(var)].get(x) for x in data[str(var)]])

    if not inplace: 
        return data
    
    else: 
        for var in variables: 
            data_dictionary[var] = data[var]