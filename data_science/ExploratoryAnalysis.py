from DataWrangling import DataWrangling
import matplotlib.pyplot as plt
import numpy as np

class ExploratoryAnalysis():     
    '''
    Visualization tool for a set of variables. 
    
    Author: Tiago Rosa dos Reis
    '''
    def __init__(self,data): 
        self.dataset   = data
        self.variables = data.columns.values
    
    def DefineGrid(self,nCols):
    
        def ComputeAllLists():

            import math

            varsList = list(self.variables)
            numVars  = len(varsList)

            nRows = math.ceil(numVars/nCols)
            remove = len(DataWrangling.ComputeRowsColumns(nRows,nCols)) - numVars

            if remove is 0: 
                ref_ = DataWrangling.ComputeRowsColumns(nRows,nCols)
            else:
                ref_ = DataWrangling.ComputeRowsColumns(nRows,nCols)[:-remove]            

            [ref_[i].insert(0,varsList[i]) for i in range(numVars)][0]

            return ref_, nRows, nCols

        nRows = ComputeAllLists()[1]
        nCols = ComputeAllLists()[2]

        d = DataWrangling.ConvertListsToTuples(ComputeAllLists()[0])
        d = DataWrangling.ConvertTuplestoDicts(d, col_index=0, p0=1, pN=4)

        return d, nRows
        
    def AllPlots(self,nCols=2,figureSize=(16,8),hist=True,kde=True,hist_bins=10,**kwargs):

        variables = list(self.variables)

        d, nRows  = self.DefineGrid(nCols)

        kde_kws = {'color':'blue',
                   'shade':False,
                   'alpha':1.0,
                   'linewidth':3,
                   'shade_lowest':True,
                   'label': 'Density'}

        hist_kws = {'color':'blue', 
                    'alpha':0.5, 
                    'edgecolor':'black', 
                    'linewidth':1.2, 
                    'label': 'Quantity'}

        import seaborn as sns

        fig, ax = plt.subplots(nRows,nCols,figsize=figureSize)

        if len(variables) is 1: 

            g = sns.distplot(self.dataset[variables[0]],ax=ax,bins=hist_bins,hist=hist,kde=kde,kde_kws=kde_kws,hist_kws=hist_kws)       

        elif len(variables) > 1: 

            for variable in variables:

                k, i, j = d.get(variable)

                if nCols is 1: 
                    axis = ax[k]
                elif(nCols) > 1 and nRows > 1: 
                    axis = ax[i,j]
                else: 
                    axis = ax[k]

                g = sns.distplot(self.dataset[variable],ax=axis,bins=hist_bins,hist=hist,kde=kde,kde_kws=kde_kws,hist_kws=hist_kws)

                sns.despine()

                plt.tight_layout()

                for item in g.get_xticklabels():
                    item.set_rotation(90)

                g.axes.set_title(str(variable), fontsize=14,color="Black",alpha=1.0)
                g.set_xlabel('Values',size=12,color='k',alpha=1.0)
                g.tick_params(labelsize=12,labelcolor='black')

                if kde is True: 
                    g.set_ylabel('Density',size=12,color='k',alpha=1.0,weight='bold')
                else: 
                    g.set_ylabel('Quantity',size=12,color='k',alpha=1.0,weight='bold')