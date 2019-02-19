import numpy as np
import pandas as pd
from DataWrangling import DataWrangling

class RandomGenerator(): 
    
    """
    This module is still under development ...
    
    
    """
    
    def __init__():
        pass

    def RandomList(limit_range,n): 
        '''
        Generates a random list of integers (starting from 0)
        '''
        import numpy as np
        import random
        empty_list = np.zeros((1,n))[0]
        return np.unique(list(map(lambda x: random.randint(0,limit_range-1), empty_list)))

    def RandomIndexGenerator(input_list,limit_range,n): 
        '''
        Returns a dictionary with random indices to each unique value of a pre-assigned random variable
        '''
        import random 

        d, all_ints = {},[]

        for i in range(len(input_list)): 

            ints = list(RandomList(limit_range,n))
            new_ints = list(filter(lambda x: x not in DataWrangling.FlatList(all_ints), ints))
            all_ints.append(ints)
            d[input_list[i]] = new_ints

        all_indices = np.arange(0,limit_range,1)
        computed_indices = DataWrangling.FlatList(d.values())
        rest = list(filter(lambda x: x not in computed_indices,all_indices))
        d[input_list[i]] = d[input_list[i]] + rest

        return d

    def InputRandomColumn(df,vars_dict): 
        '''
        Inserts new random columns in a previously assigned dataframe
        '''
        for k, v in vars_dict.items(): 

            d = RandomIndexGenerator(v,df.shape[0],df.shape[0])

            for key in d.keys(): 
                df.loc[d[key],str(k)] = str(key)