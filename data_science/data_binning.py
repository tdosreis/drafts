import numpy as np

class DataBinning(): 

    import numpy as np
    import pandas as pd
    import seaborn as sns
    from DataWrangling import DataWrangling
    
    def __init__(self,v): 
        self.vector = v
    
    def DataBins(self,bins=5,decimals=3): 
        '''
        Discretizes a list of values
        '''
        if not np.any(np.isnan(self.vector)): 
            return np.histogram(self.vector,bins=bins)[1]
        else: 
            print('NaN present in data')
    
    def MapData(self,bins=5,method='upper_bound'): 
        '''
        Computes the dictionary of values and corresponding bins
        '''
        if not np.any(np.isnan(self.vector)): 
            bins_list = DataBins(self.vector,bins)
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
    
    def DataBoundaries(self,bins=5): 
        '''
        Displays tuples with all the binarized intervals in a vector
        '''
        refs   = list(self.DataBins(bins))
        
        refs = [round(i,3) for i in refs]
        
        bounds = [tuple(refs[i:i+2]) for i in range(len(refs))][:-1]
        
        return bounds
    
    def Verbosity(self,funcs, mapping_method, j, values, boundary_mask, bounds, verbosity=False, keep_lower_bound=True,):
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
            print('Values  : '     , np.unique(self.vector))
            print('Filter  : ',((np.array(np.unique(self.vector)) <= j[1]) & (np.array(np.unique(v1)) >= j[0])))
    
            print('\n','Interval Avg: ', funcs[0],'\n','Interval Max: ', funcs[1],'\n','Interval Min: ', funcs[2],'\n')
    
            print('Filtered values: ', np.unique(self.vector)[boundary_mask])
    
            print('Mapped values: ', values)
    
            print('===========================================================================')
            print('\n')
                
    def FilterFuncsList(self,funcs_list,names_list,mapping_method): 
        '''
        Filters a list of functions based on its names
        '''
        funcs_list  = np.array(funcs_list)
        funcs_mask  = list(map(lambda x: x == mapping_method, names_list))
        
        return funcs_list[funcs_mask][0]         
    
    def TransformData(self,bins=5, verbosity=False, mapping_method='mean', keep_lower_bound=True):
        import numpy as np
        '''
        For each value in a list, attributes another value based on a discretized interval
        '''
        if not np.any(np.isnan(self.vector)):
            bounds = self.DataBoundaries(bins)
        else:
            print('NaN present in data','\n')
    
        values, mapped = [], []
    
        for j in bounds: 
            
            boundary_mask = np.where(keep_lower_bound, 
                                     ((np.array(np.unique(self.vector)) < j[1])  & (np.array(np.unique(self.vector)) >= j[0])), 
                                     ((np.array(np.unique(self.vector)) <= j[1]) & (np.array(np.unique(self.vector)) >  j[0])))
            
            funcs = [np.mean([j[1],j[0]]),(j[1]),(j[0])]
            
            function = self.FilterFuncsList(funcs,['mean','upper_bound','lower_bound'],mapping_method=mapping_method)
    
            _ = list(map(lambda x: (x,round(function,3)), np.unique(self.vector)[boundary_mask]))
    
            values.append(_)
            mapped.append(function)
    
            self.Verbosity(j=j,funcs=funcs,mapping_method=mapping_method,
                      values=_,boundary_mask=boundary_mask,bounds=bounds,
                      verbosity=verbosity,keep_lower_bound=keep_lower_bound)
    
        values = [item for sublist in values for item in sublist] 
    
        if keep_lower_bound is True and max(max(bounds)) == max(np.unique(self.vector)):
            values.append((max(np.unique(self.vector)),mapped[-1]))
    
        elif keep_lower_bound is False and min(min(bounds)) == min(np.unique(self.vector)): 
            values.insert(0,(min(np.unique(self.vector)),mapped[0]))
            
        return values
    
    def ConvertData(self,bins=5,mapping_method='mean',keep_lower_bound=True,verbosity=False,show_boundaries=False): 
        import numpy as np
        from DataWrangling import DataWrangling
        '''
        Computes the labeled intervals of a binarized vector
        '''
        if show_boundaries: 
            print('Transforming data according to the boundaries: ','\n',self.DataBoundaries(bins=bins))
        else: 
            pass
        mapping = self.TransformData(bins,mapping_method=mapping_method,keep_lower_bound=keep_lower_bound,verbosity=verbosity)
        mapping = DataWrangling().ConvertTuplestoDicts(mapping,0,1)
        
        return list(map(lambda x: mapping[x], self.vector))
    
    def LabelBins(self,data,bins=5): 
        boundaries = ['['+str(i).split('(')[1] for i in self.DataBoundaries(data,bins=bins)]
        boundaries[-1] = boundaries[-1].split(')')[0]+str(']')
        return boundaries
