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

def NS_X(i,j,u,u_tp,v,dx,dy,dt,Re):
    
            uu_1 = ((1./2.)*(u[i+1,j] + u[i,j]))**2.
            
            uu_2 = ((1./2.)*(u[i-1,j] + u[i,j]))**2.

            u_sum1 = u[i,j] + u[i,j+1]
            
            u_sum2 = u[i,j] + u[i,j-1]
            
            v_sum1 = v[i,j] + v[i+1,j]
            
            v_sum2 = v[i,j-1] + v[i+1,j-1] 
            
            uv_x1 = (1./2.)*(u_sum1)*(1./2.)*(v_sum1)
            
            uv_x2 = (1./2.)*(u_sum2)*(1./2.)*(v_sum2)
            
            D2u_x2 = ((u[i+1,j] - 2.*u[i,j] + u[i-1,j])/dx**2.)
            
            D2u_y2 = ((u[i,j+1] - 2.*u[i,j] + u[i,j-1])/dy**2.)
            
            Duu_x = (uu_1 - uu_2)/dx
            
            Duv_y = (uv_x1 - uv_x2)/dy

            ##########################
            ###### ADVECTION-X #######

            A_u =  Duu_x + Duv_y

            ####################################
            ###### DIFFUSION (Laplacian) #######

            D2_u = (D2u_x2 + D2u_y2) 
            
            ##########################
            ###### Predicted U #######
            
            u_tp[i,j] = u[i,j] + dt*(- A_u + (1./Re)*D2_u)

            return u_tp

def NS_Y(i,j,u,v_tp,v,dx,dy,dt,Re):

            vv_1 = ((1./2.)*(v[i,j+1] + v[i,j]))**2.
            
            vv_2 = ((1./2.)*(v[i,j] + v[i,j-1]))**2.

            u_sum3 = u[i,j+1] + u[i,j]

            u_sum4 = u[i-1,j+1] + u[i-1,j]

            v_sum3 = v[i,j] + v[i+1,j]

            v_sum4 = v[i,j] + v[i-1,j]           
            
            uv_y1 = (1./2.)*(u_sum3)*(1./2.)*(v_sum3)
            
            uv_y2 = (1./2.)*(u_sum4)*(1./2.)*(v_sum4)
            
            D2v_x2 = ((v[i+1,j] - 2.*v[i,j] + v[i-1,j])/dx**2.)
            
            D2v_y2 = ((v[i,j+1] - 2.*v[i,j] + v[i,j-1])/dy**2.)
            
            Duv_x = (uv_y1 - uv_y2)/dx 
            
            Dvv_y = (vv_1 - vv_2)/dy
        
            ##########################
            ###### ADVECTION-Y #######
            
            A_v = Duv_x + Dvv_y
                        
            ####################################
            ###### DIFFUSION (Laplacian) #######
            
            D2_v = (D2v_x2 + D2v_y2)
            
            ##########################
            ###### Predicted V #######
            
            v_tp[i,j] = v[i,j] + dt*(- A_v + (1./Re)*D2_v)

            return v_tp
