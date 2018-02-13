##############################################################################
##########                                                           #########
##########        ME614 - Computational Fluid Dynamics (CFD)         #########
##########                    Purdue University                      #########
##########                   Tiago Rosa dos Reis                     #########
##########             Final Project: Lid-Driven Cavity              #########
##########                       Fall 2015                           #########
##########                                                           #########
##############################################################################

##############################################################################
## The following script computes the solution of the Navier-Stokes problem  ##
## in a lid-driven cavity. The pressure and streamfunction are solved using ## 
## a SOR approach and the momentum equations are solved using an explicit   ## 
##               time-advancement scheme (Euler method, RK1).               ##
##############################################################################

#########################################
########## System Functions #############
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

#########################################
########## Basic Functions ##############
import NS
import Solver
import Plots
import Boundary_Conditions

machine_epsilon = np.finfo(float).eps

#########################################
############# User Input ################
Nxc = 128
Nyc = 128

dx = 1./Nxc  
dy = 1./Nyc 

# uniform grid
x = np.linspace(0 - dx, 1.0 + dx, Nxc+2)
y = np.linspace(0 - dy, 1.0 + dy, Nyc+2)

#[X,Y] = np.meshgrid(x,y)

Re = 1000. # Reynolds Number
tf = 20. # Final Simulation Time
SOR = 1.5 # SOR Factor
Iterations = 10. # Max. # of iterations
dt = 0.01 # Time Step

MaxErr = 0.001

N = tf/dt # of iterations for tf

#########################
###### Cavity BCs #######
Un = 1.0 # upper boundary
Us = 0.0 # bottom plate
Vw = 0.0 # left plate
Ve = 0.0 # right plate

##########################################
########### Initial Conditions ###########
c = np.zeros((Nxc+2,Nyc+2))
u = np.zeros((Nxc+1,Nyc+2))
u_tp = np.zeros((Nxc+1,Nyc+2))
v = np.zeros((Nxc+2,Nyc+1))
v_tp = np.zeros((Nxc+2,Nyc+1))
P = np.zeros((Nxc+2,Nyc+2))
P_tp = np.zeros((Nxc+2,Nyc+2))
u_contour = np.zeros((Nxc+1,Nyc+1))
v_contour = np.zeros((Nxc+1,Nyc+1))
P_contour = np.zeros((Nxc+1,Nyc+1))
phi_contour = np.zeros((Nxc+2,Nyc+2))
phi = np.zeros((Nxc+2,Nyc+2))
vorticity = np.zeros((Nxc+2,Nyc+2))
x2d = np.zeros((Nxc+2,Nyc+2))
y2d = np.zeros((Nxc+2,Nyc+2))
res = np.zeros((Nxc+2,Nyc+2))

#####################################
########## Pressure BCs #############

Boundary_Conditions.Pressure_BCs(Nxc,Nyc,c)

P_chk = np.zeros((Nxc+2,Nyc+2))

######################################
######### Time Integration ###########

t = 0 # initial time

it   = 0 # of iterations

plot_every  = 200

print "Reynolds number := "  + str(Re)

ERROR = []

for n in range (1,int(N+1)):
   
    ##########################
    ###### Velocity BCs ######

    for i in range (0,Nxc+1):
        
        for j in range (0,Nyc+1):

            Boundary_Conditions.Velocity_BCs(i,j,u,v,Us,Un,Vw,Ve,Nxc,Nyc)
        
    ###############################################
    ########### Advection & Diffusion #############
    
    for i in range (1,Nxc):
        
        for j in range (1,Nyc+1):

            u_tp = NS.NS_X(i,j,u,u_tp,v,dx,dy,dt,Re)
            
    
    for i in range (1,Nxc+1):
        
        for j in range (1,Nyc):

            v_tp = NS.NS_Y(i,j,u,v_tp,v,dx,dy,dt,Re)
  
    #########################################
    ############ Poisson Solver #############
    
    for it in range (1,int(Iterations)+1): # SOR

        #keyboard()
        
        for i in range (1,Nxc+1):

            for j in range (1,Nyc+1):

                P_chk[i,j] = P[i,j]

        #keyboard()
        
        for i in range (1,Nxc+1):

            for j in range (1,Nyc+1):

                P = Solver.Poisson(i,j,u_tp,v_tp,dx,dy,dt,P,c,SOR)

                phi = Solver.Streamline(i,j,dx,dy,dt,phi,vorticity,SOR)
                
                ##########################
                #### Pressure Ghosts #####

                Boundary_Conditions.Pressure_Ghosts(Nxc,Nyc,P)

    ##########################
    #### Residuals (RMS) #####                
                
    RMS_error = np.sqrt(np.sum(np.sum((P_chk - P)**2 ))/(Nxc*Nyc))
        
    ERROR.append(RMS_error)
    
    ##########################################
    ############# Vorticity BCs ##############
    
    for i in range (1,Nxc+1):
        
        for j in range (1,Nyc+1):
            
            Boundary_Conditions.Vorticity_BCs(i,j,Nxc,Nyc,dx,dy,phi,vorticity)
    
    ##########################################
    ########### Projection Method ############

    for i in range (1,Nxc):
    
        for j in range (1,Nyc+1):
        
            u[i,j] = u_tp[i,j] - (dt/dx)*(P[i+1,j] - P[i,j])
        
    for i in range (1,Nxc+1):
    
        for j in range (1,Nyc):
        
            v[i,j] = v_tp[i,j] - (dt/dy)*(P[i,j+1] - P[i,j])

    ##########################################
    ############## Setup Scale ###############

    x[0:Nxc+2] = np.linspace(0,Nxc,Nxc+2)
    
    y[0:Nyc+2] = np.linspace(0,Nyc,Nyc+2)
     
    for i in range (0,Nxc+2):
        
        for j in range (0,Nyc+2):
            
            x2d[i,j] = x[i]
            
            y2d[i,j] = y[j]

    ##########################################
    ############# Contour Plots ##############

    for i in range (0,Nxc+1):
    
        for j in range (0,Nyc+1):
       
            u_contour[i,j] = (1./2.) *( u[i,j] + u[i,j+1] )

            v_contour[i,j] = (1./2.) *( v[i,j] + v[i+1,j] )

            P_contour[i,j] = (1./4.) *( P[i,j] + P[i+1,j] + P[i,j+1] + P[i+1,j+1] )

            vorticity[i,j] = ( v[i+1,j] - v[i,j] )/dx - ( u[i,j+1] - u[i,j] )/dy

            phi_contour[i,j] = (1./4.) *(phi[i,j] + phi[i+1,j] + phi[i,j+1] + phi[i+1,j+1])    

    [X,Y] = np.meshgrid(x,y)
    
    STREAMLINE = np.transpose(phi_contour[0:Nxc+2,0:Nyc+2])
    
    VORTEX = np.transpose(vorticity[0:Nxc+2,0:Nyc+2])

    t += dt    

    it += 1
    
    print "Running time : " + str(t)

    #########################################
    ########## Interactive Viewer ###########
    
#    figwidth       = 10
#    figheight      = 6
#    lineWidth      = 4
#    textFontSize   = 28
#   gcafontSize    = 30
#    plt.ion()      # pylab's interactive mode-on
#    fig = plt.figure(0, figsize=(figwidth,figheight))
#    ax   = fig.add_axes([0.15,0.15,0.8,0.8])
#    if ~bool(np.mod(it,plot_every)): # plot every plot_every time steps
#       plt.cla()
#       
#       try:
#           plt.contour(STREAMLINE)
#       except ValueError:  #raised if `y` is empty.
#           pass
#
#       ax.grid('on',which='both')
#       plt.setp(ax.get_xticklabels(),fontsize=gcafontSize)
#       plt.setp(ax.get_yticklabels(),fontsize=gcafontSize)
#       plt.draw()
#       sleep(0.01)

########################################
########### Generate Plots #############

Plots.Velocity_Field(u_contour,v_contour)

Plots.Streamlines(X,Y,STREAMLINE)

Plots.U_Velocity(u_contour)

Plots.V_Velocity(v_contour)

Plots.Pressure(P_contour)

Plots.Vorticity(vorticity)
