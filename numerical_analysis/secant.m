clear all
close all
clc
%-------------------------------------------------------------------------%
% Problem 3
%-------------------------------------------------------------------------%

%---------------%
% Secant Method
%---------------%

a=pi/2;
b=pi;
nmax=50;
dig=35;
i = 0;
for tol=[.5e-7 .5e-15 .5e-33]
    
    n=0;    
    digits(dig);    
    a=vpa(a);    
    b=vpa(b);    
    x=b;
        
    while subs(abs(x-a))>=tol
        
        n = n+1;
        
        if n>nmax
            
            fprintf('n exceeds nmax')
            return
            
        end
        
        b=a;        
        fb = (1./2.)*a - sin(a);        
        a=x;        
        fa = (1./2.)*x - sin(x);        
        x = a - (a - b).*((1./2.)*a - sin(a))/(fa-fb)
        i = i + 1
        
    end
    
end
