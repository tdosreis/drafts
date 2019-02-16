clear all
close all
clc
%-------------------------------------------------------------------------%
% Problem 3
%-------------------------------------------------------------------------%

%------------------%
% Bisection Method
%------------------%

a=pi/2;
b=pi;
dig=35;

for tol=[.5e-7 .5e-15 .5e-33]
    
    ntol = ceil(log((b-a)./tol)/log(2))
    
    digits(dig);
    
    a=vpa(a);
    b=vpa(b);
    
    for n=1:ntol
        fprintf('ntol: ')
        disp(ntol)
        x=vpa((a+b)/2)
        f = (1./2.)*x - sin(x);
        fx=subs(f);
        
        if fx<0
            
            a=x;
            
        else
            
            b=x;
            
        end
%         disp(ntol)
    end
%     disp(ntol)
    
end


