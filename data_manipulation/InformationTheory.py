from collections import Counter
from DataWrangling import DataWrangling
from DataBinning import *
import numpy as np
import pandas as pd
import seaborn as sns

def ComputeProbs(data,compute_nan=False):
    '''
    Computes the probability mass function of a list of values
    '''
    if type(data) is np.ndarray: 
        data = data.tolist()
    else:
        pass
        
    N = np.where(compute_nan is False, np.sum( ~ np.isnan(data)), len(data))
    P = [(i,float(j/N)) for (i,j) in Counter(data).items()]
    P = DataWrangling.ConvertTuplestoDicts(P,0,1)
    
    if not compute_nan and np.nan in P.keys(): 
        P.pop(np.nan)
    else: 
        pass
    
    return P

def ElementWiseProbs(data,compute_nan=False,items_set=False): 
    '''
    Computes the probability of each element in a list of values
    '''
    P = ComputeProbs(data,compute_nan=compute_nan)
    
    if not items_set: 
        return list(map(lambda x: P.get(x),data))
    else: 
        return list(P.values())
    
def ShannonEntropy(data,bins,compute_nan=False,compute_bins=True):
    '''
    Shannon discrete entropy H(X) for a list of values (X)
    
    Parameters
    ==========
    ...
    
    Returns
    =======
    ...
    '''
    
    if compute_bins: 
        x = ConvertData(data,bins,show_boundaries=False)
    else: 
        x = np.array(data)
    
    probs = ElementWiseProbs(x,compute_nan=compute_nan,items_set=True)

    return -sum(list(map(lambda p: p*np.log(p), filter(None,probs))))

def DistributionPlot(vals,X,Y,x_bins,y_bins,figSize=(10,6)): 
    '''
    Plots a seaborn heatmap for binned variables X and Y
    '''
    fig, ax = plt.subplots(1,1,figsize=figSize)
    
    sns.heatmap(vals,
                cmap = 'Blues',
                ax=ax,annot=True,fmt='.3f',
                annot_kws = {'fontsize':10,'weight':'bold'},
                yticklabels = DataBinning.LabelBins(X,x_bins),
                xticklabels = DataBinning.LabelBins(Y,y_bins))
    
    ax.tick_params(labelsize = 12,labelcolor='black')

def JointProbability(X,Y,x_bins,y_bins,compute_probs=True,plot_graph=False): 
    '''
    Joint probability between X and Y variables
    '''    
    quants = np.histogram2d(X,Y,[x_bins,y_bins])[0]
    
    probs = quants/np.sum(quants)
    
    vals = np.where(compute_probs, probs, quants)
    
    if not plot_graph: 
        pass
    else: 
        DistributionPlot(vals,X,Y,x_bins,y_bins)

    return vals   
    
def JointEntropy(X,Y,x_bins,y_bins):

    probs = JointProbability(X,Y,x_bins,y_bins,compute_probs=True).ravel()

    return - (np.nansum(probs*np.log(probs)))

def MutualInformation(X,Y,x_bins,y_bins,normalized=True): 
    
    MI = ShannonEntropy(X,x_bins) + ShannonEntropy(Y,y_bins) - JointEntropy(X,Y,x_bins,y_bins)
    
    if normalized: 
        return round(MI / ShannonEntropy(Y,y_bins),4)
    else:
        return round(MI,4)

def FeatureSelection(df,target,x_bins,target_bins,method='mutual_information',normalized=True): 
    '''
    Display a ranking of the most significant variables in a dataset according to a specific method
    
    Parameters
    ==========
    ........
    
    Returns
    =======
    ........
    '''
    if method == 'mutual_information': 
        variables = df.columns.values
        return sorted([(MutualInformation(df[str(variable)],target,x_bins,target_bins,normalized=normalized), \
                        variable) for variable in variables],reverse=True)
    
#     elif method == 'information_value': 
#         return ...

