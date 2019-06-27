def FillMissingGaps(df,variable): 
    '''
    Fills missing gaps in a pandas column by adding the consecutive integer
    '''
    data  = df[str(variable)]
    nulls = data.isnull()
    
    reference_index   = data[nulls].index - 1 # previous index
    values_to_fill    = df.loc[reference_index,str(variable)] + 1 # consecutive integer
    df[str(variable)] = df[str(variable)].fillna(pd.Series(list(values_to_fill), index=nulls[nulls].index))

FillMissingGaps(df,'b')