import sys
import numpy as np
import scipy
import pylab as plt
from pdb import set_trace as keyboard
from matplotlib import rc as matplotlibrc

def Velocity_Field(u_contour,v_contour):

    ###################
    ### LaTeX Setup ###
    
    matplotlibrc('text.latex', preamble='\usepackage{color}')
    matplotlibrc('text',usetex=True)
    matplotlibrc('font', family='serif')

    figure_folder = "../report/"   
    
    figure_name = "velocity_field.pdf"

    figwidth       = 6
    figheight      = 6
    lineWidth      = 3
    textFontSize   = 16
    gcafontSize    = 30

    fig = plt.figure(0, figsize=(figwidth,figheight))

    plt.quiver(np.flipud(np.rot90(u_contour)),np.flipud(np.rot90(v_contour)))
    
    plt.title("Velocity Field", fontsize=textFontSize)
        
    figure_file_path = figure_folder + figure_name
    print "Saving figure: " + figure_file_path
    plt.tight_layout()
    plt.savefig(figure_file_path)   
    plt.close()

def Streamlines(X,Y,STREAMLINE):

    ###################
    ### LaTeX Setup ###
    
    matplotlibrc('text.latex', preamble='\usepackage{color}')
    matplotlibrc('text',usetex=True)
    matplotlibrc('font', family='serif')

    figure_folder = "../report/"   
    
    figure_name = "streamlines.pdf"

    figwidth       = 6
    figheight      = 6
    lineWidth      = 3
    textFontSize   = 16
    gcafontSize    = 30

    fig = plt.figure(0, figsize=(figwidth,figheight))

    plt.contour(X,Y,STREAMLINE,100)
    
    plt.title("Streamlines", fontsize=textFontSize)
        
    figure_file_path = figure_folder + figure_name
    print "Saving figure: " + figure_file_path
    plt.tight_layout()
    plt.savefig(figure_file_path)   
    plt.close()

def U_Velocity(u_contour):
    
    ###################
    ### LaTeX Setup ###
    
    matplotlibrc('text.latex', preamble='\usepackage{color}')
    matplotlibrc('text',usetex=True)
    matplotlibrc('font', family='serif')

    figure_folder = "../report/"   
    
    figure_name = "u_velocity.pdf"

    figwidth       = 6
    figheight      = 6
    lineWidth      = 3
    textFontSize   = 16
    gcafontSize    = 30

    fig = plt.figure(0, figsize=(figwidth,figheight))

    plt.contour(np.rot90(np.fliplr(u_contour)),100)
    
    plt.title("U-Velocity", fontsize=textFontSize)
        
    figure_file_path = figure_folder + figure_name
    print "Saving figure: " + figure_file_path
    plt.tight_layout()
    plt.savefig(figure_file_path)   
    plt.close()

def V_Velocity(v_contour):
    
    ###################
    ### LaTeX Setup ###
    
    matplotlibrc('text.latex', preamble='\usepackage{color}')
    matplotlibrc('text',usetex=True)
    matplotlibrc('font', family='serif')

    figure_folder = "../report/"   
    
    figure_name = "v_velocity.pdf"

    figwidth       = 6
    figheight      = 6
    lineWidth      = 3
    textFontSize   = 16
    gcafontSize    = 30

    fig = plt.figure(0, figsize=(figwidth,figheight))

    plt.contour(np.rot90(np.fliplr(v_contour)),100)
    
    plt.title("V-Velocity", fontsize=textFontSize)
        
    figure_file_path = figure_folder + figure_name
    print "Saving figure: " + figure_file_path
    plt.tight_layout()
    plt.savefig(figure_file_path)   
    plt.close()

def Pressure(P_contour):
    
    ###################
    ### LaTeX Setup ###
    
    matplotlibrc('text.latex', preamble='\usepackage{color}')
    matplotlibrc('text',usetex=True)
    matplotlibrc('font', family='serif')

    figure_folder = "../report/"   
    
    figure_name = "pressure.pdf"

    figwidth       = 6
    figheight      = 6
    lineWidth      = 3
    textFontSize   = 16
    gcafontSize    = 30

    fig = plt.figure(0, figsize=(figwidth,figheight))

    plt.contour(np.rot90(np.fliplr(P_contour)),100)
    
    plt.title("Pressure", fontsize=textFontSize)
        
    figure_file_path = figure_folder + figure_name
    print "Saving figure: " + figure_file_path
    plt.tight_layout()
    plt.savefig(figure_file_path)   
    plt.close()

def Vorticity(vorticity):
    
    ###################
    ### LaTeX Setup ###
    
    matplotlibrc('text.latex', preamble='\usepackage{color}')
    matplotlibrc('text',usetex=True)
    matplotlibrc('font', family='serif')

    figure_folder = "../report/"   
    
    figure_name = "vorticity.pdf"

    figwidth       = 6
    figheight      = 6
    lineWidth      = 3
    textFontSize   = 16
    gcafontSize    = 30

    fig = plt.figure(0, figsize=(figwidth,figheight))

    plt.contour(np.rot90(np.fliplr(vorticity)),100)
    
    plt.title("Vorticity", fontsize=textFontSize)
        
    figure_file_path = figure_folder + figure_name
    print "Saving figure: " + figure_file_path
    plt.tight_layout()
    plt.savefig(figure_file_path)   
    plt.close()
    

    
