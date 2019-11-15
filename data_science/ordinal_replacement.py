def GetIndex(x): 
    '''
    Extracts the index of a specific value in a list
    '''
    return np.where(np.array(list(x))=='F')[0]
    
def Replacements(x): 
    '''
    Creates a list of ordinals to be replaced
    '''
    return np.arange(1,len(x)+1,1)
    
def Mapping(keys,values): 
    '''
    Concatenates separate keys and values into a dictionary (mapping) structure
    '''
    return {k: v for k,v in zip(keys,values)}
    
def ToStr(data):    
    '''
    Converts list of values into str
    '''
    return "".join(map(str,data))
    
def Modify(x,keys,values): 
    '''
    Association between index and values
    '''
    for (k, v) in zip(keys,values): 
        x[k] = v
    return ToStr(list(x))

%python
    
df.A = df.A.apply(lambda x: list(x))
df.A.apply(lambda x: Modify(x,GetIndex(x),Replacements(GetIndex(x))))

# df.A.apply(lambda x: Modifyy(x,Mapping(GetIndex(x),Replacements(x))))