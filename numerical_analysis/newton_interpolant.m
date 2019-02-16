% Problem 3
%-----------%

close all
clear all
clc

figure % creates figure first, then iterates into the loop

t = linspace(-5,5,101);

npts = [2,4,6,8]; 

% Interpolant (Newton)
%----------------------%
for n = npts    
    
    i = linspace(0,npts(end),npts(end)+1);
    
    x = -5 + 10*i/n;
    
    T = 1./(1 + x.^2);
    
    for j = 1:n
        
        for i = fliplr((linspace(j,n,n-j+1)))
            
            T(i+1) = ( T(i + 1) - T(i) )/( x(i + 1) - x(i + 1 - j) );
            
        end
        
    end
    
    y = T(n+1);
    
    for i = fliplr(linspace(1,n,n))
        
        y = T(i) + (t - x(i)).*y;
        
    end
    
    plot(t,y,'b-','LineWidth',2.0)
    
    hold on
    
    plot(t,1./(1 + t.^2),'r--','LineWidth',3.0)
    
end


