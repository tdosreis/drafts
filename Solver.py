import os
import sys
import numpy as np
import scipy.sparse as scysparse
from pdb import set_trace as keyboard
from time import sleep
import scipy.sparse as scysparse
import scipy.sparse.linalg as spysparselinalg  # sparse linear algebra
import scipy.linalg as scylinalg               # non-sparse linear algebra
import pylab as plt
from matplotlib import rc as matplotlibrc
import time # has the equivalent of tic/toc

def Poisson(i,j,u_tp,v_tp,dx,dy,dt,P,c,SOR):

        ##########################
        ## Conservation of Mass ##
        
        COM = (u_tp[i,j] - u_tp[i-1,j] + v_tp[i,j] - v_tp[i,j-1])
        
        ##########################
        ##### Pressure Terms #####
        
        Pressure = (P[i+1,j] + P[i-1,j] + P[i,j+1] + P[i,j-1])
        
        ##########################
        ##### 'Poisson Eqn' ######
        
        P[i,j] = SOR*(c[i,j])*(Pressure - (dx/dt)*(COM)) + (1.0 - SOR)*P[i,j]

        return P

def Streamline(i,j,dx,dy,dt,phi,vorticity,SOR):

        ############################
        ##### 'Streamfunction' #####
        
        PHI = (phi[i+1,j] + phi[i-1,j] + phi[i,j+1] + phi[i,j-1])
                       
        phi[i,j] = (1./4.)*SOR*(PHI + (dx*dy)*vorticity[i,j]) + (1.0 - SOR)*phi[i,j]

        return phi
