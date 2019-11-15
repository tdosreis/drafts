import numpy as np

class EvalMetrics():     
    '''
    Alternative class for model evaluation: quantifying the quality of predictions
    
    Author: Tiago Rosa dos Reis
    
    Note: code is still under development
    '''
    def __init__(self,y_true,y_pred): 
        self.y_true = np.array(y_true)
        self.y_pred = np.array(y_pred)
        
    def ComputeKS(self): 
        '''
        Computes the Kolmogorov-Smirnov test for an ML model
        '''
        from scipy import stats
        return stats.ks_2samp(self.y_pred[self.y_true==1.0],self.y_pred[self.y_true==0.0])[0]
        
    def ComputeAccuracy(self): 
        '''
        Alternative approach to compute the accuracy of a model
        '''
        f = lambda x: 1 if x[0] == x[1] else 0
        x = zip(self.y_true,self.y_pred)
        trues = list(map(f,x))
        return sum(trues)/len(trues)

    def ZeroMatrix(self): 
        '''
        Computes the skeleton matrix for all lists of combinations
        '''
        import numpy as np

        dim = len(np.unique(self.y_true))

        return np.zeros((1,dim,dim))[0] 

    def Combinations(self,n_combinations=2): 
        '''
        Computes all combinations in a list of values
        '''
        import itertools
        import numpy as np

        list_of_values = np.unique(self.y_true)

        # identity combinations
        a = list(map(lambda x: (x,x),list_of_values))

        # ordered combinations
        b = list(itertools.combinations(list_of_values,n_combinations))

        # reverse order combinations
        c = list(map(lambda x: tuple(sorted(x,reverse=True)),b)) 

        return sorted(sum([a,b,c],[]))

    def MapIndices(self): 
        '''
        Computes the indices of each value in a vector 
        '''
        return {j:i for (i,j) in enumerate(np.unique(self.y_true))}

    def GetIndices(self,x):
        '''
        Extracts the indices in a list of tuples 
        '''
        ix = self.MapIndices()
        return tuple([ix.get(x[i]) for i in range(len(x))])

    def Transform(self,n_combinations=2):
        '''
        Converts the combination of values to a combination of indices
        '''
        return {i: self.GetIndices(i) for i in self.Combinations(n_combinations=2)}

    def SumMaps(self): 
        '''
        Computes the summation of values for each key in a map
        '''
        return {i:sum(list(map(lambda x: x == i, list(zip(self.y_true,self.y_pred))))) for i in self.Combinations()}

    def ConvertMaps(self): 
        '''
        Converts a map of tuples into a map of indices
        '''
        ix          = self.MapIndices()
        coordinates = self.Transform()
        sum_maps    = self.SumMaps()
        return {coordinates.get(i): sum_maps.get(i) for i in sum_maps}

    def ConfusionMatrix(self): 
        '''
        Generalized form of the confusion matrix between y_true and y_pred
        '''
        map_to_map = self.ConvertMaps()

        M = self.ZeroMatrix()
        
        for i in map_to_map: 
            M[i] = map_to_map.get(i)

        return M

    def ConvertToBinary(self,thresh=.5): 
        '''
        Converts a list of continuous probabilities into discrete (binary) values
        '''
        return list(map(lambda x: 1 if x > thresh else 0, self.y_true))

    def RandomProbs(self,length): 
        '''
        Generates a list of random probabilty values
        '''
        return [random.random() for i in range(length)]
    
    