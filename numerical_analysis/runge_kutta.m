%-------------------------------------------------------------------------%
%Problem 2
%-------------------------------------------------------------------------%
close all
clear all
clc
format long
%-------------------------------------------------------------------------%
%Input Setup
%-------------------------------------------------------------------------%
mu = 0.0122771171;
n = [1000, 5000, 10000, 50000, 100000];
Tf = 17.1;
A = cell(1,length(n));

figure

for j = 1:length(n)
    
    dt = Tf/n(j);
    
    % Initial Conditions
    %-------------------%
    time = 0;
    u1 = 0.994;
    u2 = 0;
    du1dt = 0;
    du2dt = -2.00158510637908252240537862224;
    u = [u1 u2 du1dt du2dt];
    
    v = @(t, u)...
        [u(2); ...
        u(1) + 2*u(4) - (1 - mu)*(u(1) + mu)./((u(1) + mu)^2 + u(3)^2)^(3/2)...
        - mu*(u(1) - (1 - mu))*((u(1) - (1 - mu))^2 + u(3)^2)^(-3/2);...
        u(4);...
        u(3) - 2*u(2) - (1 - mu)*u(3)*((u(1) + mu)^2 + u(3)^2)^(-3/2)...
        - mu*u(3)./((u(1) - (1 - mu))^2 + u(3)^2)^(3/2)];
    
    U = u';
    
    i = 1;
    
    %---------------------------------------------------------------------%
    % Runge-Kutta 4th order
    %---------------------------------------------------------------------%
    
    while time <= Tf
        
        K1 = U(:,i);
        U1 = v(dt*i, K1);
        
        K2 = U(:,i) + (dt/2)*v(dt*i, K1);
        U2 = v(dt*(i+1/2), K2);
        
        K3 = U(:,i) + (dt/2)*v(dt*(i+1/2), K2);
        U3 = v(dt*(i+1/2), K3);
        
        K4 = U(:,i) + dt*v(dt*(i+1/2), K3);
        U4 = v(dt*(i+1), K4);  
        
        U(:,i+1) = U(:,i) + (dt/6)*(U1 + 2*U2 + 2*U3 + U4);
        
        time = time + dt;
        
        i = i + 1;
        
    end
    
    %---------------------------------------------------------------------%
    % Plot Results
    %---------------------------------------------------------------------%
    A{1,j} = U;
    
    Y = A{1,j};
    
    if j == 1
        p1 = plot(Y(1,:),Y(3,:),'r-','LineWidth',2.0);
        hold on
    end
    if j == 2
        p2 = plot(Y(1,:),Y(3,:),'b-','LineWidth',2.0);
        hold on
    end
    if j == 3
        p3 = plot(Y(1,:),Y(3,:),'k-','LineWidth',2.0);
        hold on
    end
    if j == 4
        p4 = plot(Y(1,:),Y(3,:),'g-','LineWidth',1.0);
        hold on
    end
    if j == 5
        p5 = plot(Y(1,:),Y(3,:),'m-','LineWidth',1.0);
        hold on
    end
end

l1 = legend([p1 p2 p3 p4 p5],{'$n=1000$','$n=5000$',...
    '$n=10000$','$n=50000$','$n=100000$'},'Interpreter','LaTex');
set(l1,'FontSize',12)
hold on
x1 = xlabel('$u_{1}$','Interpreter','LaTex');
set(x1,'FontSize',16)
y1 = ylabel('$u_{2}$','Interpreter','LaTex');
set(y1,'FontSize',16)

Y1=A{1,1}; Y2=A{1,2}; Y3=A{1,3}; Y4=A{1,4}; Y5=A{1,5};
figure
p1 = plot(Y1(1,:),Y1(3,:),'r-','LineWidth',2.0);
figure
p2 = plot(Y2(1,:),Y2(3,:),'b-','LineWidth',2.0);
figure
p3 = plot(Y3(1,:),Y3(3,:),'k-','LineWidth',2.0);
figure
p4 = plot(Y4(1,:),Y4(3,:),'g-','LineWidth',1.0);
figure
p5 = plot(Y5(1,:),Y5(3,:),'m-','LineWidth',1.0);

hold on
x1 = xlabel('$u_{1}$','Interpreter','LaTex');
set(x1,'FontSize',16)
y1 = ylabel('$u_{2}$','Interpreter','LaTex');
set(y1,'FontSize',16)



