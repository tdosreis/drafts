clear all
close all
clc
%-------------------------------------------------------------------------%
% Problem 3
%-------------------------------------------------------------------------%

%-----------------------%
% False Position Method
%-----------------------%
a=pi/2;
b=pi;
nmax=100;
dig=37;

for tol=[.5e-7 .5e-15 .5e-33]
    
    n=0;    
    digits(dig);    
    a=vpa(a);     
    b=vpa(b);    
    fa = (1./2.)*a - sin(a);
    fb = (1./2.)*b - sin(b);
    
    while subs(b-a)>=tol
        
        n = n+1
        
        if n>nmax
            
            fprintf('n exceeds nmax')
            return
        end
        
        x = a-(a-b)*fa/(fa - fb)
        
        fx = (1./2.)*x - sin(x); %f(x)
        
        if abs(subs(fx))<tol
            return
        end
        
        if subs(fx*fa)>0
            a=x; 
            fa=fx;            
        else
            b=x; 
            fb=fx;
        end
        
    end
    
end
