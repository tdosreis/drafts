%-------------------------------------------------------------------------%
% Problem 3.5
%-------------------------------------------------------------------------%
close all
clear all
clc
format long
%-------------------------------------------------------------------------%
% Input Setup
%-------------------------------------------------------------------------%
a = -1.;
b = 1.;

% Analytical Values of Integration
% [x^20,e^x,exp-x^2,1/(1+16*x^2),exp(-1/x^2),|x|^3]
I_wolfram = [0.09523809523809, 2.35040238728760, 1.49364826562485, ...
    0.66290883183401623252961960521423781559, ...
    0.17814771178156, 0.50000000000000];

%--------------------%
% Monte Carlo Method %
%--------------------%
N= [];
n = 1;

while n <= 1000
    
    
    n_mc = round(rand(1)*1000); % random number of "n" points
    x_mc = linspace(a,b,n_mc);
    
    f1_mc = x_mc.^20;
    f2_mc = exp(x_mc);
    f3_mc = exp(-x_mc.^2);
    f4_mc = 1./(1. + 16.*(x_mc.^2.));         % not even close to
    f5_mc = exp(-1./(x_mc.^2));             % the most efficient
    f6_mc = abs(x_mc.^3);                   % code ...
    
    I1_mc = (b-a)*mean(f1_mc); % Numerical Integral (Monte Carlo)
    
    I2_mc = (b-a)*mean(f2_mc); % Numerical Integral (Monte Carlo)
    
    I3_mc = (b-a)*mean(f3_mc); % Numerical Integral (Monte Carlo)
    
    I4_mc = (b-a)*mean(f4_mc); % Numerical Integral (Monte Carlo)
    
    I5_mc = (b-a)*mean(f5_mc); % Numerical Integral (Monte Carlo)
    
    I6_mc = (b-a)*mean(f6_mc); % Numerical Integral (Monte Carlo)
    
    N(n) = n_mc;
    
    I1(n) = I1_mc;
    I2(n) = I2_mc;
    I3(n) = I3_mc;
    I4(n) = I4_mc;
    I5(n) = I5_mc;
    I6(n) = I6_mc;
    
    n = n+1
    
end    

figure
plot(N,I1,'ro','LineWidth',1.0);
hold on
plot(N,I2,'bo','LineWidth',1.0);
hold on
plot(N,I3,'ko','LineWidth',1.0);
hold on
plot(N,I4,'ms','LineWidth',1.0);
hold on
plot(N,I5,'gs','LineWidth',1.0);
hold on
plot(N,I6,'ys','LineWidth',1.0);
hold on
ylabel('Numerical Integration (Monte Carlo)')
xlabel('N uniform divisions (random)')

legend('x^20','e^x','exp(-x^2)','1/(1+16*x^2)','exp(-1/x^2)','|x|^3')

var1 = var(I1)
var2 = var(I2)
var3 = var(I3)
var4 = var(I4)
var5 = var(I5)
var6 = var(I6)

