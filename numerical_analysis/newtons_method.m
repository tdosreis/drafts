%-------------------------------------------------------------------------%
% Problem 3
%-------------------------------------------------------------------------%
close all
clear all
clc
%-------------------------------------------------------------------------%
% Kepler's equation
%-------------------------------------------------------------------------%

% Newton's Method
%-----------------%
e = [0.3 0.5 0.7];
t = linspace(0,20);
for j = 1:length(t)
    for i = 1:length(e)
        u  = t(j);
        U(i,j) = u - (u-e(i)*sin(u)- t(j))/(1 - e(i)*cos(u));
    end
end

% General Solutions
%-------------------%
x1 = cos(U) - e(1).*ones(size(U));
x2 = cos(U) - e(2).*ones(size(U));
x3 = cos(U) - e(3).*ones(size(U));
y1 = (sqrt(1.*ones(size(U))) - ((e(1).*ones(size(U))).^2)).*sin(U);
y2 = (sqrt(1.*ones(size(U))) - ((e(2).*ones(size(U))).^2)).*sin(U);
y3 = (sqrt(1.*ones(size(U))) - ((e(3).*ones(size(U))).^2)).*sin(U);

figure
p1 = plot(t,x1(1,:),'r-','LineWidth',2.0)
hold on
p2 = plot(t,x2(2,:),'b-','LineWidth',2.0)
hold on
p3 = plot(t,x3(3,:),'k-','LineWidth',2.0)
ylabel('X(t)','Interpreter','Latex','FontSize',14)
xlabel('time (t)','Interpreter','Latex','FontSize',14)
l1 = legend([p1 p2 p3],{'$\epsilon = 0.3$',...
    '$\epsilon = 0.7$','$\epsilon = 0.7$'},'Interpreter','LaTex');
set(l1,'FontSize',10)

figure
p1 = plot(t,y1(1,:),'r-','LineWidth',2.0)
hold on
p2 = plot(t,y2(2,:),'b-','LineWidth',2.0)
hold on
p3 = plot(t,y3(3,:),'k-','LineWidth',2.0)
ylabel('Y(t)','Interpreter','Latex','FontSize',14)
xlabel('time (t)','Interpreter','Latex','FontSize',14)
l1 = legend([p1 p2 p3],{'$\epsilon = 0.3$',...
    '$\epsilon = 0.7$','$\epsilon = 0.7$'},'Interpreter','LaTex');
set(l1,'FontSize',10)




