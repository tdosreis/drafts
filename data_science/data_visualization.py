import matplotlib.pyplot as plt
import numpy as np
from DataWrangling import DataWrangling, Operations

class StatisticalPlots(): 
    '''
    A collection of various statistical plots
    
    Author: Tiago Rosa dos Reis
    '''
    def __init__(self,):
        pass
    
    def TargetPlot(self,data,target,figSize=(10,10)):
        '''
        Plots the customized histogram distribution of a binary target variable.
        '''
        print('Percentage of (binary target): ',str(round(float(target.sum())/data.shape[0],2)*100),str('%'))

        fig, ax = plt.subplots(1,1,figsize=figSize)

        fig.suptitle('Histogram for target',fontsize=16,weight='bold',color='black')

        y_distance = (data.shape[0] - target.sum())*0.025

        arr = np.array(target)

        labels, counts = np.unique(arr, return_counts = True)

        ax.bar(labels, counts, align='center',color='lightblue',edgecolor='darkblue',linewidth=1)
        ax.set_xticks(labels)
        ax.set_xlabel('Values',fontsize=14,weight='bold')
        ax.set_ylabel('Quantity',fontsize=14,weight='bold')
        ax.set_xticklabels(labels,fontsize=14,weight='bold')
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

        for p in ax.patches:
            width, height = p.get_width(), p.get_height()
            x, y = p.get_xy() 
            ax.annotate('{:.2%}'.format(float(height)/data.shape[0]),
                        (p.get_x()+.35*width, p.get_y() + height + y_distance),
                        fontsize=12,weight='bold',color='darkgreen')
    
    import seaborn as sns

    def BoxPlotAllValues(self,data,figureSize=(16,8),vert=True): 
        '''
        Boxplot of all variables within 'data'. Must be a dataframe.
        '''
        d = {i:data[i] for i in data.columns.values}

        fig, ax = plt.subplots(1,1,figsize=figureSize)
        ax.boxplot(d.values(),
                   notch=False, 
                   sym='k.', 
                   vert=vert, 
                   whis=1.5, 
                   positions=None, 
                   widths=0.5, 
                   patch_artist=True, 
                   meanline=True, 
                   showmeans=True, 
                   showcaps=True, 
                   showbox=True,
                   showfliers=True,
                   boxprops=dict(facecolor='lightblue', color='black'),
                   capprops=dict(color='black'),
                   whiskerprops=dict(color='black'),
                   medianprops=dict(color='k'),
                   meanprops=dict(color='red'),
                   flierprops={'color':'darkgreen','alpha':0.8,'markersize':2,'markeredgecolor': 'darkgreen','marker': '.'})
        if vert: 
            ax.set_xticklabels(d.keys(),rotation=90)
        elif not vert: 
            ax.set_yticklabels(d.keys(),rotation=0)
        fig.tight_layout(rect=[0, 0.05, 1, 0.95])
        fig.suptitle('Outlier distribution per variable',fontsize=14,weight='bold')

    def PlotStats(self,data,boxPlot=True,linePlot=True,scatterPlot=True,histPlot=True,
                  histBins=100,figureSize=(12,8),plotTitle = None,verbosity=False,axis=None): 
        '''
        Generalized plotting function, includes boxplot, scatterplot, lineplot, histogram for data visualization of a single variable
        '''    
        def boxplot_(ax,): 
            ax.boxplot(data,
                       notch=True, 
                       sym='k.', 
                       vert=False, 
                       whis=1.5, 
                       positions=None, 
                       widths=0.5, 
                       patch_artist=True, 
                       meanline=True, 
                       showmeans=True, 
                       showcaps=True, 
                       showbox=True,
                       showfliers=True,
                       boxprops=dict(facecolor='lightblue', color='black'),
                       capprops=dict(color='black'),
                       whiskerprops=dict(color='black'),
                       medianprops=dict(color='k'),
                       meanprops=dict(color='red'),
                       flierprops={'color':'darkgreen','alpha':0.8,'markersize':2,'markeredgecolor': 'darkgreen','marker': '.'})
            ax.set_xlabel('Values',fontsize=10,weight='bold')
    #         ax.set_ylabel('Teste',fontsize=10,weight='bold')
            ax.set_title('BoxPlot',fontsize=12,weight='bold')

        def lineplot_(ax,): 
            ax.plot(dataIndex,data, 
                    color='green', 
                    marker='o', 
                    linestyle='dashed',
                    linewidth=0.05, 
                    markersize=0.1)
            ax.set_xlabel('Index',fontsize=10,weight='bold')
            ax.set_ylabel('Values',fontsize=10,weight='bold')
            ax.set_title('LinePlot',fontsize=12,weight='bold')

        def scatterplot_(ax,): 
            ax.scatter(dataIndex,data,
                            s=1.0, 
                            c='darkred', 
                            marker='o')
            ax.set_xlabel('Index',fontsize=10,weight='bold')
            ax.set_ylabel('Values',fontsize=10,weight='bold')
            ax.set_title('ScatterPlot',fontsize=12,weight='bold')

        def histogramplot_(ax,): 
            ax.hist(data,
                    bins=histBins, 
                    range=None, 
                    density=None, 
                    weights=None, 
                    cumulative=False, 
                    bottom=None, 
                    histtype='bar', 
                    align='mid', 
                    orientation='vertical', 
                    rwidth=None, 
                    log=False, 
                    color='darkblue', 
                    label=None, 
                    stacked=False, 
                    normed=None)
            ax.set_xlabel('Values',fontsize=10,weight='bold')
            ax.set_ylabel('Quantity',fontsize=10,weight='bold')
            ax.set_title('Histogram',fontsize=12,weight='bold')
            
        
        dataIndex = range(len(data)) # scatterPlot, linePlot ...
        inputList = np.array([boxPlot,  linePlot,  scatterPlot,  histPlot])
        funcList  = np.array([boxplot_, lineplot_, scatterplot_, histogramplot_])
        allFuncs  = funcList[inputList]

        reference_ = [(4,(2,2)),(3,(2,2)),(2,(1,2)),(1,(1,1))]

        nRows, nCols = [i[1] for i in reference_ if i[0] == len(allFuncs)][0]

        fig, axes = plt.subplots(nRows,nCols,figsize=figureSize)

        axesList = [list(np.hstack(axes)) if len(allFuncs) > 1 else [axes]][0]

        for i in range(len(allFuncs)):
            allFuncs[i](axesList[i])

        if verbosity is True:
            '''
            Put other stuff here ...
            '''
            print('Total number of plots: ',len(allFuncs),'\n')
        else:
            pass

        if plotTitle is None:
            fig.suptitle('Data Analysis',fontsize=16)
        else:
            fig.suptitle('Data Analysis for ' + str(plotTitle),fontsize=16)

        fig.tight_layout(rect=[0, 0.05, 1, 0.95])
        
        
    def CompareCorrelation(self,original_data,treated_data,figureSize=(12,4),title='',correlation_method = 'pearson'):         
        '''
        Compares the correlation coefficent distribution among two different datasets.
        '''
        fig, ax = plt.subplots(1,2,figsize=figureSize, sharex=True, sharey=True)

        import seaborn as sns

        correlationsList = [original_data.corr(),treated_data.corr()]

        vmin = min([i.min() for i in [i.min().values for i in correlationsList]])

        cbar_ax = fig.add_axes([.9, .2, .03, .65])

        for i,correlation in enumerate(correlationsList):

            sns.heatmap(correlation,
                        cmap='gist_gray_r',
                        ax=ax[i],
                        cbar=i == 0,
                        cbar_ax=None if i else cbar_ax,
                        annot=True,
                        vmin=vmin,
                        vmax=1,
                        fmt='.2f',
                        annot_kws={'size':10,'weight':'bold'})

        ax[0].set_title('Original data')
        ax[1].set_title('Treated data')

        fig.suptitle('Correlation comparison: ' + str(title),fontsize=16)

        fig.tight_layout(rect=[0, 0.03, 0.9, 0.95])
        
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

            nRows = int(math.ceil(float(numVars)/nCols))
            remove = len(DataWrangling().ComputeRowsColumns(nRows,nCols)) - numVars
            
            if remove == 0: 
                ref_ = DataWrangling().ComputeRowsColumns(nRows,nCols)
            else:
                ref_ = DataWrangling().ComputeRowsColumns(nRows,nCols)[:-remove]            
            [ref_[i].insert(0,varsList[i]) for i in range(int(numVars))][0]

            return ref_, nRows, nCols
            
        
        nRows = ComputeAllLists()[1]
        nCols = ComputeAllLists()[2]

        d = DataWrangling().ConvertListsToTuples(ComputeAllLists()[0])
        d = DataWrangling().ConvertTuplestoDicts(d, col_index=0, p0=1, pN=4)
        
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
                    
                    
def main(): 
    '''
    Put some code here...
    '''
    
if __name__ == '__main__': 
    main()
    print('Data Visualization running as main script')
else:
    print('Data Visualization imported from another module')