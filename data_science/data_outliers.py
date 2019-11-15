import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class AnalyzeOutliers():
    '''
    Computes the indices of the outlier values based on each criterion
    
    Author: Tiago Rosa dos Reis
    '''
    def __init__(self,data):
        
        self.data       = data
        self.mean       = np.mean(self.data)
        self.median     = np.median(self.data)
        self.standDev   = np.std(self.data)
        self.meanAbsDev = np.median(np.abs(self.data - self.median))
        
    def OutlierZScore(self,threshold=3.0):
        '''
        Computes the indices of the corresponding outlier values according to zscore
        '''
        zScore = (self.data - self.mean)/(self.standDev)
        self.zScoreOutlier = np.where(np.abs(zScore) > threshold,)
        return self.zScoreOutlier[0], self.data[self.zScoreOutlier[0]].min()
    
    def OutlierModifiedZScore(self,threshold=3.5):
        '''
        Computes the indices of the corresponding outlier values according to modified-zscore
        '''
        modZScore = (0.6745)*((self.data - self.median))/(self.meanAbsDev)
        self.ModZScoreOutlier = np.where(np.abs(modZScore) > threshold,)
        return self.ModZScoreOutlier[0], self.data[self.ModZScoreOutlier[0]].min()
    
    def OutlierIQR(self,):
        '''
        Computes the indices of the corresponding outlier values according to IQR
        '''
        firstQuartile, thirdQuartile = np.percentile(self.data, [25, 75])
        iqr = thirdQuartile - firstQuartile
        lowerBound = firstQuartile - (iqr*1.5)
        upperBound = thirdQuartile + (iqr*1.5)
        self.iqrOutlier = np.where((self.data > upperBound) | (self.data < lowerBound))
        return self.iqrOutlier[0], upperBound
    
    '''
    Add different criterion for outlier detection...
    '''
    
    def OutlierPlot(self,figureSize=(12,4),plotTitle=None,ZScore=True,ModZScore=True,IQR=True):
        
        import seaborn as sns
        import matplotlib.pyplot as plt   
        
        mask = np.array([ZScore,ModZScore,IQR])
        
        outIndex = np.array([('ZScore',self.OutlierZScore()[0],self.OutlierZScore()[1]),
                             ('ModifiedZScore',self.OutlierModifiedZScore()[0],self.OutlierModifiedZScore()[1]),
                             ('IQR',self.OutlierIQR()[0],self.OutlierIQR()[1])],dtype=object) #arbitrary types within array
        
        outIndex = outIndex[mask]
        
        for i in outIndex:
            fig, ax = plt.subplots(1,2,figsize=figureSize)
            
            fig.suptitle(str(plotTitle) + ' Outlier Analysis: ' + i[0],fontsize=14)
            
            sizeOne = np.array(self.data/self.mean)
            sizeTwo = np.array(self.data[i[1]]/self.mean)
            
            sizeOne[abs(sizeOne) > 20] = 20
            sizeTwo[abs(sizeTwo) > 20] = 20

            ax[0].scatter(self.data.index, self.data, s=sizeOne, c='lightblue')
            ax[0].scatter(i[1], self.data[i[1]], s=sizeTwo, c='darkblue')
            ax[0].plot(self.data.index,[i[2]]*len(self.data.index),'r-.',linewidth=3.0)
            ax[0].set_xlabel('Index',weight='bold')
            ax[0].set_ylabel('Values',weight='bold')
            ax[0].set_title('ScatterPlot')

            sns.distplot(self.data,hist=False,ax=ax[1],norm_hist=True,)
            ax[1].plot(self.data[i[1]],[0.]*len(self.data[i[1]]),'ro',ms=7.5)
            ax[1].set_xlabel('Values',weight='bold')
            ax[1].set_ylabel('Distribution',weight='bold')
            ax[1].set_title('Density DistPlot')
            
            out_quant = float(len(i[1]))
            all_quant = float(len(self.data))
            pct_quant = (out_quant/all_quant)*100
                    
            fig.text(0.75,0.75,'Number of outliers: ' + str(out_quant), fontsize=12, weight='bold',color='darkgreen')
            fig.text(0.75,0.70,'[%] of outliers: ' + str(round(pct_quant,2))+'%', fontsize=12, weight='bold',color='darkgreen')
            
            fig.tight_layout(rect=[0, 0.03, 1, 0.95])
                    
    def ComputeOutliers(self): 
        return self.OutlierZScore()[0], self.OutlierModifiedZScore()[0], self.OutlierIQR()[0]
    
    def RemoveOutliers(self,title='',show_original=True,show_zscore=True,show_modzscore=True,show_iqr=True): 

        import seaborn as sns
        import pandas as pd

        ZScore, ModZScore, IQR = self.ComputeOutliers()

        fig, ax = plt.subplots(1,2,figsize=(16,5))

        fig.suptitle('Outlier Removal: ' + str(title), fontsize=16)

        sns.distplot(self.data.drop(ZScore,axis=0),ax=ax[0], hist=False, kde=True,
                     kde_kws={'color':'red','shade':False,'alpha':0.6,'linewidth':5,'shade_lowest':True,'label': 'ZScore'})

        sns.distplot(self.data.drop(ModZScore,axis=0),ax=ax[0],hist=False,kde=True,
                     kde_kws={'color':'blue','shade':False,'alpha':0.6,'linewidth':5,'shade_lowest':True,'label': 'ModZScore'})

        sns.distplot(self.data.drop(IQR,axis=0),ax=ax[0],hist=False,kde=True,
                     kde_kws={'color':'green','shade':False,'alpha':0.6,'linewidth':5,'shade_lowest':True,'label': 'IQR'})
        
        mask = np.array([show_original,show_zscore,show_modzscore,show_iqr])
        
        dataList   = np.array([self.data,self.data.drop(ZScore),self.data.drop(ModZScore),self.data.drop(IQR)],dtype=object)
        dataList   = dataList[mask]
        dataLabel  = np.array(['Original Data','ZScore','ModZScore','IQR'])
        dataLabel  = dataLabel[mask]
        dataColors = np.array(['black', 'red', 'blue', 'green'])
        dataColors = dataColors[mask]

        boxes = ax[1].boxplot(dataList,
                              showfliers=True,vert=False,whis=1.5,positions=None,widths=0.5,patch_artist=True, 
                              meanline=True,showmeans=True,showcaps=True,showbox=True,
                              boxprops=dict(facecolor='lightblue', color='black'),
                              capprops=dict(color='black'),whiskerprops=dict(color='black'),
                              medianprops=dict(color='k'),meanprops=dict(color='red'),
                              flierprops={'alpha':0.8,'markersize':5,'markeredgecolor': 'None','marker': '.'})

        for f, fc in zip(boxes['fliers'], dataColors):
            f.set_markerfacecolor(fc)

        ax[1].set_yticklabels(dataLabel, fontsize=12, weight='bold')
        ax[1].set_xlabel('Values',weight='bold',fontsize=14)

        ax[1].tick_params(labelsize=14,labelcolor='black')

        ax[0].tick_params(labelsize=14,labelcolor='black')
        ax[0].set_xlabel('Values',weight='bold',fontsize=14)

        plt.setp(ax[0].get_legend().get_texts(), fontsize='16') 
        plt.setp(ax[0].get_legend().get_title(), fontsize='32')

        fig.tight_layout(rect=[0, 0.03, 1, 0.95])
        
        plt.show()
        
class TreatOutliers():
    '''
    Removes the outliers of a given dataset using a specific criterion: {IQR, ZScore, ModZScore}
    '''
    def __init__(self,):
        pass
    
    def DropOutliers(self,data,method='IQR'):
        '''
        Removes the outlier values in accordance to each selected method: {IQR, ZScore, ModZScore}
        '''
        methodsList = {'ZScore':0,'ModZScore':1,'IQR':2}
        print('Dropping outliers using: ', method)
        return data.drop(AnalyzeOutliers(data).ComputeOutliers()[methodsList.get(method)])

    def DropAllOutliers(self,data,method='IQR'): 
        '''
        Applies DropOutliers() function to a set of variables within a dataframe
        '''
        print()
        if len(data.shape) == 1: 
            print('Removing Outliers: ',data.name)
            return self.DropOutliers(data,method=method)
        else:
            varsList = data.columns
            print('Removing Outliers: ',varsList.values)
            return data.apply(lambda x: self.DropOutliers(x,method=method))

    def MethodNaN(self,x): 
        return {'median':x.median(),'mean':x.mean(),'zero':0}

    def ReplaceNaN(self,data,method='median'): 
        if len(data.shape) == 1: 
            return data.fillna(data.median())
        else:
            return data.apply(lambda x: x.fillna(self.MethodNaN(x).get(method))) 


def main(): 
    '''
    Put some code here...
    '''
    
if __name__ == '__main__': 
    main()
    print('Data Outliers running as main script')
else:
    print('Data Outliers imported from another module')