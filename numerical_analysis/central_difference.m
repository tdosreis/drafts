% Problem 5

close all
clear all
clc

% Analytical functions

x1 = linspace(0,5,10000);
x2 = linspace(-5,5,10000);
x3 = linspace(0,1,10000);

y1 = exp(x1);
y2 = 1./(1. + x2.^2);
y3 = ((exp(3.*x3)).*sin(200.*(x3.^2)))./(1. + 20.*x3.^2);

% Analytical derivatives (exact)

d1 = exp(x1);
d2 = -(2.*x2)./((x2.^2 + 1.).^2);
d3 = (3.*exp(3.*x3).*sin(200.*x3.^2.))./(20.*x3.^2.+1.) - ...
    (40.*(exp(3.*x3)).*x3.*sin(200.*x3.^2.))/((20.*x3.^2.+1.).^2.) + ...
    (400.*(exp(3.*x3)).*x3.*cos(200.*x3.^2))./((20.*x3.^2.+1.));

% Central Difference Formula
%-----------------------------%

h = [10^-10, 10^-7, 10^-4, 10^-1];
emax = zeros(length(h),1);
figure
for i = 1:4
        
    p1 = (exp(x1+h(i)) - exp(x1-h(i)))./(2.*h(i));
    
    plot(x1,d1,'k-','LineWidth',2.0)
    hold on
    plot(x1,p1,'b--','LineWidth',3.0)
    
    emax(i) = max(abs(p1 - d1));
    
    
    
end
figure
plot(h,emax,'k-','LineWidth',2.0)
xlabel('h')
ylabel('emax')


emax = zeros(length(h),1);
figure
for i = 1:4
    
    p2 = ((1./(1. + (x2+h(i)).^2)) - (1./(1. + (x2-h(i)).^2)))./(2.*h(i));
    
    plot(x2,d2,'k-','LineWidth',2.0)
    hold on
    plot(x2,p2,'b--','LineWidth',3.0)
    
    emax(i) = max(abs(p2 - d2));
    
end
figure
plot(h,emax,'k-','LineWidth',2.0)
xlabel('h')
ylabel('emax')

emax = zeros(length(h),1);
figure
for i=1:4
    
    p3 = ((((exp(3.*(x3+h(i)))).*sin(200.*((x3+h(i)).^2)))./(1. + 20.*(x3+h(i)).^2)) - ...
        (((exp(3.*(x3-h(i)))).*sin(200.*((x3-h(i)).^2)))./(1. + 20.*(x3-h(i)).^2)))./(2.*h(i));
    
    plot(x3,d3,'k-','LineWidth',2.0)
    hold on
    plot(x3,p3,'b--','LineWidth',3.0)
    
    emax(i) = max(abs(p3 - d3));
    
end
figure
plot(h,emax,'k-','LineWidth',2.0) 
xlabel('h')
ylabel('emax')
