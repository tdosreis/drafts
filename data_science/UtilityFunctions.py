# This module is currently under development ...

# Module created to unify all sorts of functions and data science tools for data wrangling and processing

import pandas as pd
import numpy as np

def AggregateValues(df,map_opers): 
    '''
    Applies functions in a groupby operation
    '''
    import pandas as pd

    d = {}
    for var, l_oper in map_opers.items(): 
        for op in l_oper: 
            d[''.join([str(op),'_',str(var)])] = float(df[str(var)].agg([op]))
    
    return pd.Series(d,index=list(d.keys()))


# e.g. use
# map_opers = {
#     'LIMIT_BAL':['mean','count'],
#     'BILL_AMT2':['max','median']
# }
# AggregateValues(df,map_opers)
# >>> mean_LIMIT_BAL      167484.322667
# >>> count_LIMIT_BAL      30000.000000
# >>> max_BILL_AMT2       983931.000000
# >>> median_BILL_AMT2     21200.000000
# >>> dtype: float64

def ListValues(values): 
    '''
    Extracts the list of values in a dictionary
    '''
    return list(np.array(list((key_words.values())),dtype=object).ravel())
    
def GetSubStrings(list_of_substrings, list_of_variables): 
    '''
    Extracts a list of variables with substrings matching a second list of variables
    '''
    return list(np.unique([i for j in list_of_substrings for i in list_of_variables if j in i]))

def CatchSubVariables(key_words,list_of_variables):
    '''
    Transforms an input dictionary containing a list of substrings into a dictionary
    with the corresponding variables in a larger list
    
    Input
    =====
    key_words: dictionary wth list of substrings
    
    list_of_variables: reference list for which one wants to filter the names contained in the dictionary of substrings
    
    Output
    ======
    A final dictionary with the corresponding keys
    
    Author: Tiago Rosa dos Reis
    '''
    list_of_substrings = ListValues(key_words)
    strs = GetSubStrings(list_of_substrings,list_of_variables)
    return {str(i):[v for k in j for v in strs if k in v] for i,j in key_words.items()}

# e.g. use
# key_words = {'payment':['pay','Pay','PAY'],
#              'bill':   ['Bill','bill','BILL'],
#              'limit':  ['LIM','Lim','lim'],
#              'amount': ['Amt','AMT','amt']
#             }

# CatchSubVariables(key_words,df.columns.values)['bill']

# >>> ['BILL_AMT1', 'BILL_AMT2', 'BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6']


def GenRandInts(n=10,x=(1,10)): 
    '''
    Generates a list of random integers
    '''
    import random
    if n > (np.sum([x[1] - x[0],1])): 
        print('n has to be smaller than values range! ')
        pass
    else:
        numbers, aux = [],[]
        while len(number)<n: 
            number = random.randint(x[0],x[1])
            if number not in aux: 
                numbers.append(number)
            else:pass
            aux.append(number)
        return numbers

def GenRandVals(values,n=10): 
    '''
    Generates a list of values based on random indices
    '''
    print('List of random values')
    ixs = GenRandInts(n,(0,len(values)))
    return values[ixs]
    
def GetRandIxs(df,variable,n=10):
    '''
    Generates a list of random indices corresponding to random IDs
    '''
    u_vals = df[variable]
    return (df.loc[df[variable].isin(GenRandVals(u_vals,n)),:].index)   







