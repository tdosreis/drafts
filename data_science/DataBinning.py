from DataWrangling import DataWrangling
import numpy as np
import pandas as pd
import seaborn as sns

def DataBins(v,bins=5,decimals=3): 
    '''
    Discretizes a list of values
    '''
    if not np.any(np.isnan(v)): 
        return np.histogram(v,bins=bins)[1]
    else: 
        print('NaN present in data')

def MapData(v,bins=5,method='upper_bound'): 
    '''
    Computes the dictionary of values and corresponding bins
    '''
    if not np.any(np.isnan(v)): 
        bins_list = DataBins(v,bins)
    else: 
        print('NaN present in data')
        
    counter = 0
    list_of_dicts = []
    while counter < len(bins_list) - 1:
        
        UpperBound  = bins_list[counter + 1]
        LowerBound  = bins_list[counter]
        MeanValue   = np.mean([bins_list[counter + 1],bins_list[counter]])
        
        funcs = np.array([UpperBound, LowerBound, MeanValue])
        mask  = list(map(lambda x: x == method, ['upper_bound','lower_bound','mean']))
        
        list_of_dicts.append({funcs[mask][0]:('(' + (str(bins_list[counter])) + ' - ' + (str(bins_list[counter+1])) + ']')})
        counter += 1

    mapping = {k: v for d in list_of_dicts for k, v in d.items()}
    return mapping

def DataBoundaries(v,bins=5): 
    '''
    Displays tuples with all the binarized intervals in a vector
    '''
    refs   = list(DataBins(v,bins))
    
    refs = [round(i,3) for i in refs]
    
    bounds = [tuple(refs[i:i+2]) for i in range(len(refs))][:-1]
    
    return bounds

def Verbosity(v, funcs, mapping_method, j, values, boundary_mask, bounds, verbosity=False, keep_lower_bound=True,):
    if not verbosity:
        pass
    elif verbosity:
        
        funcs = [np.mean([j[1],j[0]]),(j[1]),(j[0])]
        
        if keep_lower_bound: 
            print('Interval cutting strategy: lower_bound')
        else: 
            print('Interval cutting strategy: upper_bound')
            
        print('Values mapping strategy: ', mapping_method)
        
        print('===========================================================================')    
        print('Boundary: '   , j)
        print('Values  : '     , np.unique(v))
        print('Filter  : ',((np.array(np.unique(v)) <= j[1]) & (np.array(np.unique(v1)) >= j[0])))

        print('\n','Interval Avg: ', funcs[0],'\n','Interval Max: ', funcs[1],'\n','Interval Min: ', funcs[2],'\n')

        print('Filtered values: ', np.unique(v)[boundary_mask])

        print('Mapped values: ', values)

        print('===========================================================================')
        print('\n')
            
def FilterFuncsList(funcs_list,names_list,mapping_method): 
    '''
    Filters a list of functions based on its names
    '''
    funcs_list  = np.array(funcs_list)
    funcs_mask  = list(map(lambda x: x == mapping_method, names_list))
    
    return funcs_list[funcs_mask][0]         

def TransformData(v, bins=5, verbosity=False, mapping_method='mean', keep_lower_bound=True): 
    '''
    For each value in a list, attributes another value based on a discretized interval
    '''
    if not np.any(np.isnan(v)):
        bounds = DataBoundaries(v,bins)
    else:
        print('NaN present in data','\n')

    values, mapped = [], []

    for j in bounds: 
        
        boundary_mask = np.where(keep_lower_bound, 
                                 ((np.array(np.unique(v)) < j[1])  & (np.array(np.unique(v)) >= j[0])), 
                                 ((np.array(np.unique(v)) <= j[1]) & (np.array(np.unique(v)) >  j[0])))
        
        funcs = [np.mean([j[1],j[0]]),(j[1]),(j[0])]
        
        function = FilterFuncsList(funcs,['mean','upper_bound','lower_bound'],mapping_method=mapping_method)

        _ = list(map(lambda x: (x,round(function,3)), np.unique(v)[boundary_mask]))

        values.append(_)
        mapped.append(function)

        Verbosity(v=v,j=j,funcs=funcs,mapping_method=mapping_method,
                  values=_,boundary_mask=boundary_mask,bounds=bounds,
                  verbosity=verbosity,keep_lower_bound=keep_lower_bound)

    values = [item for sublist in values for item in sublist] 

    if keep_lower_bound is True and max(max(bounds)) == max(np.unique(v)):
        values.append((max(np.unique(v)),mapped[-1]))

    elif keep_lower_bound is False and min(min(bounds)) == min(np.unique(v)): 
        values.insert(0,(min(np.unique(v)),mapped[0]))
        
    return values

def ConvertData(v,bins=5,mapping_method='mean',keep_lower_bound=True,verbosity=False,show_boundaries=False): 
    '''
    Computes the labeled intervals of a binarized vector
    '''
    from DataWrangling import DataWrangling
    if show_boundaries: 
        print('Transforming data according to the boundaries: ','\n',DataBoundaries(v,bins=bins))
    else: 
        pass
    mapping = TransformData(v,bins,mapping_method=mapping_method,keep_lower_bound=keep_lower_bound,verbosity=verbosity)
    mapping = DataWrangling.ConvertTuplestoDicts(mapping,0,1)
    
    return list(map(lambda x: mapping[x], v))

def LabelBins(data,bins=5): 
    boundaries = ['['+str(i).split('(')[1] for i in DataBoundaries(data,bins=bins)]
    boundaries[-1] = boundaries[-1].split(')')[0]+str(']')
    return boundaries