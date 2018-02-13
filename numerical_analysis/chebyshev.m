% Chebyshev Polynomial of the First Kind

close all
clear all
clc

n = 1:1001;

x = linspace(-1,1);

T(size(n),size(x)) = zeros;

% Chebyshev function

disp('Starting Chebyshev Recurrence Function ...')

for i = 1:n(end)
    
    if n(i) == 1
        T(n(i),:) = ones(size(x));
    end
    
    if n(i) == 2
        T(n(i),:) = x;
    end
    
    if n(i) >= 3
        T(n(i),:) = 2.*x.*T(n(i-1),:) - T(n(i-2),:);
    end
        
end

disp('Starting Chebyshev points of 1st kind ...')

% Chebyshev POINTS of the 1st kind (x-zeros of the function T)

first_kind = [];

for i = 1:n(end)
    
    for k = 1:n(i)
        
        x_k = cos(((2.*k-1)/(2.*n(i)))*pi);
        
        first_kind(n(i)+1,k) = x_k; % make sure rows are the same for T
        
    end
    
end

disp('Starting Chebyshev points of 2nd kind ...')

% Chebyshev POINTS of the 2nd kind (x-extrema of the function T)

second_kind = [];

for i = 1:n(end)
    
    for k = 0:n(i) % make sure n+1 extrema
        
        y_k = cos((k/(n(i)))*pi);
        
        second_kind(n(i)+1,k+1) = y_k;
        
    end
    
end

% Implementation of the interpolant polynomial

pts = linspace(1,5,1000);
x1 = linspace(1,5,10);
f = exp(-x1);
y = interp1(x1,f,pts);
            
  
