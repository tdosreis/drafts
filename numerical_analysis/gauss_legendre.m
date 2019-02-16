%-------------------------------------------------------------------------%
%Problem 2
%-------------------------------------------------------------------------%
close all
clear all
clc
% format long
%-------------------------------------------------------------------------%
%Input Setup
%-------------------------------------------------------------------------%
a = -1.;
b = 1.;
Nx = input('Nx : ');
Ny = input('Ny : ');
W(Nx,Ny) = zeros;
I_analytical = [2.66667 0.4444 8.5574 216]
for i = 1:length(Nx)
    
    for j = 1:length(Ny)
        
        disp('Gauss Legendre Y')
        %-----------------------------%
        % Gauss-Legendre Quadrature Y %
        %-----------------------------%
        betay = .5./sqrt(1-(2*(1:Ny(j))).^(-2)); % 3-term recurrence coeffs
        Ty = diag(betay,1) + diag(betay,-1); % Jacobi matrix
        [Vy,Dy] = eig(Ty); % eigenvalue decomposition
        y_gl = diag(Dy);
        [y_gl,j] = sort(y_gl); % nodes (= Legendre points)
        w_gl_y = 2*Vy(1,j).^2; % weights

        disp('Gauss Legendre X')
        %-----------------------------%
        % Gauss-Legendre Quadrature X %
        %-----------------------------%
        betax = .5./sqrt(1-(2*(1:Nx(i))).^(-2)); % 3-term recurrence coeffs
        Tx = diag(betax,1) + diag(betax,-1); % Jacobi matrix
        [Vx,Dx] = eig(Tx); % eigenvalue decomposition
        x_gl = diag(Dx);
        [x_gl,i] = sort(x_gl); % nodes (= Legendre points)
        w_gl_x = 2*Vx(1,i).^2; % weights     

    end
end

for i = 1:Nx
    
    for j = 1:Ny
        
        W(i,j) = w_gl_x(i).*w_gl_y(j)';
        
    end
    
end

% Functions
for i=1:Nx
    
    for j = 1:Ny
        
        f1(i,j) = x_gl(i).^2 + y_gl(j).^2;
        f2(i,j) = (x_gl(i).^2).*(y_gl(j).^2);
        f3(i,j) = exp(x_gl(i).^2 + y_gl(j).^2);
        f4(i,j) = (1. - x_gl(i).^2) + 100.*(y_gl(j)-x_gl(i).^2.)^2.;
        
    end
    
end

% Integrals
I1 = sum(f1.*W);
I1 = sum(I1)
I2 = sum(f2.*W);
I2 = sum(I2)
I3 = sum(f3.*W);
I3 = sum(I3)
I4 = sum(f4.*W);
I4 = sum(I4)
