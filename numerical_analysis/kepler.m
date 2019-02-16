close all
clear all
clc

n = [50, 120, 200, 500, 1000];
Tf = 20.0;
t_axis = cell(1,length(n));
%-------------------------------------------------------------------------%
% Kepler's equation
%-------------------------------------------------------------------------%
A = cell(1,length(n));
for k = 1:length(n)
    % Newton's Method
    %-----------------%
    e = [0.3 0.5 0.7];
    t = linspace(0,Tf,n(k));
    t_axis{1,k} = t;
    for j = 1:length(t)
        for i = 1:length(e)
            u_1  = t(j);
            U_1(i,j) = u_1 - (u_1-e(i)*sin(u_1)- t(j))/(1 - e(i)*cos(u_1));
        end
    end
    
    % General Solutions
    %-------------------%
    x1 = cos(U_1) - e(1).*ones(size(U_1));
    x2 = cos(U_1) - e(2).*ones(size(U_1));
    x3 = cos(U_1) - e(3).*ones(size(U_1));
    X = [x1(1,:);x2(2,:);x3(3,:)];
    y1 = (sqrt(1.*ones(size(U_1))) - ((e(1).*ones(size(U_1))).^2)).*sin(U_1);
    y2 = (sqrt(1.*ones(size(U_1))) - ((e(2).*ones(size(U_1))).^2)).*sin(U_1);
    y3 = (sqrt(1.*ones(size(U_1))) - ((e(3).*ones(size(U_1))).^2)).*sin(U_1);
%     X = [y1(1,:);y2(2,:);y3(3,:)];
    A{1,k} = X;
    
end

B = cell(1,length(n));

for j = 1:length(n)
    
    dt = Tf/n(j);
    
    e = 0.3;
%     e = 0.5;
%     e = 0.7;
    
    % Initial Conditions
    %-------------------%
    time = 0;
    u1 = 1 - e;
    u2 = 0;
    du1dt = 0;
    du2dt = sqrt((1+e)/(1-e));
    u = [u1 u2 du1dt du2dt];
    
    v = @(t, u)...
        [u(2); ...
        -u(1)./((sqrt(u(1)^2+u(3)^2))^3);...
        u(4);...
        -u(3)./((sqrt(u(1)^2+u(3)^2))^3)];
    
    U = u';
    i = 1;
    
    %---------------------------------------------------------------------%
    % Euler's Method
    %---------------------------------------------------------------------%
    
    while time <= Tf
        
        U(:,i+1) = U(:,i) + (dt)*v(dt*i, U(:,i));
        
        time = time + dt;
        
        i = i + 1;
    end
    B{1,j} = U;
%     Y = B{1,j};
    
end
Z1 = A{1,1};Z2 = A{1,2};Z3 = A{1,3};Z4 = A{1,4};Z5 = A{1,5};
Y1=B{1,1}; Y2=B{1,2}; Y3=B{1,3}; Y4=B{1,4}; Y5=B{1,5};
t1 = t_axis{1,1}; t2 = t_axis{1,2};t3 = t_axis{1,3};t4 = t_axis{1,4};t5 = t_axis{1,5};
E1 = Z1(1,:) - Y1(2,1:end-2);
E2 = Z2(1,:) - Y2(2,1:end-1);
E3 = Z3(1,:) - Y3(2,1:end-1);
E4 = Z4(1,:) - Y4(2,1:end-2);
E5 = Z5(1,:) - Y5(2,1:end-2);
% error
figure
plot(t1,Z1(1,:),'r-.','LineWidth',2.0)
hold on
plot(t1,Y1(2,1:end-2),'b-.','LineWidth',2.0)
hold on
plot(t2,Z2(1,:),'r--','LineWidth',2.0)
hold on
plot(t2,Y2(2,1:end-1),'b--','LineWidth',2.0)
hold on
plot(t3,Z3(1,:),'r-.','LineWidth',2.0)
hold on
plot(t3,Y3(2,1:end-1),'b-.','LineWidth',2.0)
hold on
plot(t4,Z4(1,:),'r:','LineWidth',2.0)
hold on
plot(t4,Y4(2,1:end-2),'b:','LineWidth',2.0)
hold on
plot(t5,Z5(1,:),'r-','LineWidth',2.0)
hold on
plot(t5,Y5(2,1:end-2),'b-','LineWidth',2.0)
hold on
title('$\epsilon = 0.3$','Interpreter','Latex','FontSize',14)
xlabel('time (t)','Interpreter','Latex','FontSize',14)

figure
plot(t1,E1,'b-.','LineWidth',2.0)
hold on
plot(t2,E2,'m-.','LineWidth',2.0)
hold on
plot(t3,E3,'g--','LineWidth',2.0)
hold on
plot(t4,E4,'r:','LineWidth',2.0)
hold on
plot(t5,E5,'k-','LineWidth',2.0)
hold on
title('error ($e = 0.3$)','Interpreter','Latex','FontSize',14)
xlabel('time (t)','Interpreter','Latex','FontSize',14)

% figure 
% plot(t1,Z1(1,:),'r-.','LineWidth',2.0)
% hold on
% plot(t1,Y1(2,1:end-2),'b-.','LineWidth',2.0)
% hold on
% plot(t2,Z2(1,:),'r--','LineWidth',2.0)
% hold on
% plot(t2,Y2(2,1:end-1),'b--','LineWidth',2.0)
% hold on
% plot(t3,Z3(1,:),'r-.','LineWidth',2.0)
% hold on
% plot(t3,Y3(2,1:end-1),'b-.','LineWidth',2.0)
% hold on
% plot(t4,Z4(1,:),'r:','LineWidth',2.0)
% hold on
% plot(t4,Y4(2,1:end-2),'b:','LineWidth',2.0)
% hold on
% plot(t5,Z5(1,:),'r-','LineWidth',2.0)
% hold on
% plot(t5,Y5(2,1:end-2),'b-','LineWidth',2.0)
% hold on
% title('$\epsilon = 0.5$','Interpreter','Latex','FontSize',14)
% xlabel('time (t)','Interpreter','Latex','FontSize',14)
% 
% figure
% plot(t1,E1,'b-.','LineWidth',2.0)
% hold on
% plot(t2,E2,'m-.','LineWidth',2.0)
% hold on
% plot(t3,E3,'g--','LineWidth',2.0)
% hold on
% plot(t4,E4,'r:','LineWidth',2.0)
% hold on
% plot(t5,E5,'k-','LineWidth',2.0)
% hold on
% title('error ($\epsilon = 0.5$)','Interpreter','Latex','FontSize',14)
% xlabel('time (t)','Interpreter','Latex','FontSize',14)



% figure
% plot(t1,Z1(3,:),'r-.','LineWidth',2.0)
% hold on
% plot(t1,Y1(2,1:end-2),'b-.','LineWidth',2.0)
% hold on
% plot(t2,Z2(3,:),'r--','LineWidth',2.0)
% hold on
% plot(t2,Y2(2,1:end-1),'b--','LineWidth',2.0)
% hold on
% plot(t3,Z3(3,:),'r-.','LineWidth',2.0)
% hold on
% plot(t3,Y3(2,1:end-1),'b-.','LineWidth',2.0)
% hold on
% plot(t4,Z4(3,:),'r:','LineWidth',2.0)
% hold on
% plot(t4,Y4(2,1:end-2),'b:','LineWidth',2.0)
% hold on
% plot(t5,Z5(3,:),'r-','LineWidth',2.0)
% hold on
% plot(t5,Y5(2,1:end-2),'b-','LineWidth',2.0)
% hold on
% title('$\epsilon = 0.7$','Interpreter','Latex','FontSize',14)
% xlabel('time (t)','Interpreter','Latex','FontSize',14)
% 
% figure
% plot(t1,E1,'b-.','LineWidth',2.0)
% hold on
% plot(t2,E2,'m-.','LineWidth',2.0)
% hold on
% plot(t3,E3,'g--','LineWidth',2.0)
% hold on
% plot(t4,E4,'r:','LineWidth',2.0)
% hold on
% plot(t5,E5,'k-','LineWidth',2.0)
% hold on
% title('error ($\epsilon = 0.7$)','Interpreter','Latex','FontSize',14)
% xlabel('time (t)','Interpreter','Latex','FontSize',14)

