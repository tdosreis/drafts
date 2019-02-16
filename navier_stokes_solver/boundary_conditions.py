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

def Pressure_BCs(Nxc,Nyc,c):

    c[2:Nxc,2:Nyc] = 1./4.

    c[1,1] = 1./2.
    
    c[Nxc,1] = 1./2.
    
    c[1,Nyc] = 1./2.
    
    c[Nxc,Nyc] = 1./2.

    c[2:Nxc,1] = 1./3.
    
    c[1,2:Nyc] = 1./3.
    
    c[Nxc,2:Nyc] = 1./3.
    
    c[2:Nxc,Nyc] = 1./3.

    return c

def Velocity_BCs(i,j,u,v,Us,Un,Vw,Ve,Nyc,Nxc):
    
    u[i,0] = 2.*Us - u[i,1]
    
    u[i,Nyc+1] = 2.*Un - u[i,Nyc]
    
    u[0,j+1] = 0.
    
    u[Nxc,j+1] = u[0,j+1] 

    v[0,j] = 2.*Vw - v[1,j]
    
    v[Nxc+1,j] = 2.*Ve - v[Nxc,j]
    
    v[i+1,0] = 0.
    
    v[i+1,Nyc] = v[i+1,0]

    return v

    return u

def Pressure_Ghosts(Nxc,Nyc,P):
    
    P[0:Nxc+2,0] = 0
    
    P[0:Nxc+2,Nyc+1] = 0
    
    P[0,0:Nyc+2] = 0
    
    P[Nxc+1,0:Nyc+2] = 0

    return P    

def Vorticity_BCs(i,j,Nxc,Nyc,dx,dy,phi,vorticity):
    
    vorticity[i,0] = - 2.0*phi[i,1]/(dx*dy)
    
    vorticity[i,Nyc+1]= - 2.0*phi[i,Nyc]/(dx*dy) - 2.0/dx
    
    vorticity[0,j]= - 2.0*phi[1,j]/(dx*dy)
    
    vorticity[Nxc+1,j]= - 2.0*phi[Nxc,j]/(dx*dy)

    return vorticity
