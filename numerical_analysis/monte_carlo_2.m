%-------------------------------------------------------------------------%
%Problem 3
%-------------------------------------------------------------------------%
close all
clear all
clc
format long
%-------------------------------------------------------------------------%
%Input Setup
%-------------------------------------------------------------------------%
a = -1.;
b = 1.;
N = [2. 3. 4. 5. 6. 7. 8. 9. 10 11. 12. 13. 14. 15. 16. ...
    17. 18. 19. 20. 21. 22. 23. 24. 25. 26. 27. 28. 29. 30.];

% Analytical Values of Integration
% [x^20,e^x,exp-x^2,1/(1+16*x^2),exp(-1/x^2),|x|^3]
I_wolfram = [0.09523809523809, 2.35040238728760, 1.49364826562485, ...
    0.66290883183401623252961960521423781559, ...
    0.17814771178156, 0.50000000000000];

method = [1 2 3];
N_mc = [];
n = 1;
for index=1:length(method)
    
    if method(index)==1
        
        while n<1000
            disp('Monte Carlo')
            %--------------------%
            %Monte Carlo Method %
            %--------------------%
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
            
            N_mc(n) = n_mc;
            
            I1(n) = I1_mc; 
            I2(n) = I2_mc; 
            I3(n) = I3_mc; 
            I4(n) = I4_mc; 
            I5(n) = I5_mc; 
            I6(n) = I6_mc; 
            
            n = n+1
        end
        
    end
    
    error1_mc = I1 - I_wolfram(1);
    sort(error1_mc); fliplr(error1_mc);
    error2_mc = I2 - I_wolfram(2);
    sort(error2_mc); fliplr(error2_mc);
    error3_mc = I3 - I_wolfram(3);
    sort(error3_mc); fliplr(error3_mc);
    error4_mc = I4 - I_wolfram(4);
    sort(error4_mc); fliplr(error4_mc);
    error5_mc = I5 - I_wolfram(5);
    sort(error5_mc); fliplr(error5_mc);
    error6_mc = I6 - I_wolfram(6);
    sort(error6_mc); fliplr(error6_mc);
    
    
    if method(index)==2
        
        for j = 1:length(N)
            
            disp('Clenshaw Curtis')
            %----------------------------%
            % Clenshaw-Curtis Quadrature %
            %----------------------------%
            c = zeros(N(j) + 1,2);
            c(1:2:(N(j) + 1),1) = (2./[1 1-(2:2:N(j)).^2 ])';
            c(2,2) = 1;
            f_cc = real(ifft([c(1:(N(j)+1),:);c(N(j):-1:2,:)]));
            w_cc = (b - a)*([f_cc(1,1); 2*f_cc(2:N(j),1); f_cc((N(j) + 1),1)])/2;
            x_cc = 0.5*((b + a) + N(j)*(b - a)*f_cc(1:(N(j) + 1),2));
            w_cc = w_cc';
            
            f1_cc = x_cc.^20;
            f2_cc = exp(x_cc);
            f3_cc = exp(-x_cc.^2);
            f4_cc = 1./(1. + 16.*(x_cc.^2.));         % not even close to
            f5_cc = exp(-1./(x_cc.^2));             % the most efficient
            f6_cc = abs(x_cc.^3);                   % code ...
            
            I1_cc(j) = w_cc*f1_cc; % Numerical Integral (Gauss Legendre)
            error1_cc(j) = abs(I1_cc(j) - I_wolfram(1));
            
            I2_cc(j) = w_cc*f2_cc; % Numerical Integral (Gauss Legendre)
            error2_cc(j) = abs(I2_cc(j) - I_wolfram(2));
            
            I3_cc(j) = w_cc*f3_cc; % Numerical Integral (Gauss Legendre)
            error3_cc(j) = abs(I3_cc(j) - I_wolfram(3));
            
            I4_cc(j) = w_cc*f4_cc; % Numerical Integral (Gauss Legendre)
            error4_cc(j) = abs(I4_cc(j) - I_wolfram(4));
            
            I5_cc(j) = w_cc*f5_cc; % Numerical Integral (Gauss Legendre)
            error5_cc(j) = abs(I5_cc(j) - I_wolfram(5));
            
            I6_cc(j) = w_cc*f6_cc; % Numerical Integral (Gauss Legendre)
            error6_cc(j) = abs(I6_cc(j) - I_wolfram(6));
            
        end
        
    end
    
    if method(index)==3
        
        for j = 1:length(N)
            
            disp('Gauss Legendre')
            %---------------------------%
            % Gauss-Legendre Quadrature %
            %---------------------------%
            beta = .5./sqrt(1-(2*(1:N(j))).^(-2)); % 3-term recurrence coeffs
            T = diag(beta,1) + diag(beta,-1); % Jacobi matrix
            [V,D] = eig(T); % eigenvalue decomposition
            x_gl = diag(D);
            [x_gl,i] = sort(x_gl); % nodes (= Legendre points)
            w_gl = 2*V(1,i).^2; % weights
            
            f1_gl = x_gl.^20;
            f2_gl = exp(x_gl);
            f3_gl = exp(-x_gl.^2);
            f4_gl = 1./(1. + 16.*(x_gl.^2.));
            f5_gl = exp(-1./(x_gl.^2));
            f6_gl = abs(x_gl.^3);
            
            I1_gl(j) = w_gl*f1_gl; % Numerical Integral (Gauss Legendre)
            error1_gl(j) = abs(I1_gl(j) - I_wolfram(1));
            
            I2_gl(j) = w_gl*f2_gl; % Numerical Integral (Gauss Legendre)
            error2_gl(j) = abs(I2_gl(j) - I_wolfram(2));
            
            I3_gl(j) = w_gl*f3_gl; % Numerical Integral (Gauss Legendre)
            error3_gl(j) = abs(I3_gl(j) - I_wolfram(3));
            
            I4_gl(j) = w_gl*f4_gl; % Numerical Integral (Gauss Legendre)
            error4_gl(j) = abs(I4_gl(j) - I_wolfram(4));
            
            I5_gl(j) = w_gl*f5_gl; % Numerical Integral (Gauss Legendre)
            error5_gl(j) = abs(I5_gl(j) - I_wolfram(5));
            
            I6_gl(j) = w_gl*f6_gl; % Numerical Integral (Gauss Legendre)
            error6_gl(j) = abs(I6_gl(j) - I_wolfram(6));
            
        end
        
    end
    
end

figure

subplot(3,2,1)
semilogy(N,error1_cc,'ro','LineWidth',2.0)
hold on
semilogy(N,error1_gl,'bo','LineWidth',2.0)
% hold on
% semilogy(N_mc,error1_mc,'ko','LineWidth',2.0)
xlabel('N')
ylabel('|I-I_n|')
legend('C-C','G-L','M-C')

subplot(3,2,2)
semilogy(N,error2_cc,'ro','LineWidth',2.0)
hold on
semilogy(N,error2_gl,'bo','LineWidth',2.0)
% hold on
% semilogy(N_mc,error2_mc,'ko','LineWidth',2.0)
xlabel('N')
ylabel('|l-l_n|')
legend('C-C','G-L','M-C')

subplot(3,2,3)
semilogy(N,error3_cc,'ro','LineWidth',2.0)
hold on
semilogy(N,error3_gl,'bo','LineWidth',2.0)
% hold on
% semilogy(N_mc,error3_mc,'ko','LineWidth',2.0)
xlabel('N')
ylabel('|l-l_n|')
legend('C-C','G-L','M-C')

subplot(3,2,4)
semilogy(N,error4_cc,'ro','LineWidth',2.0)
hold on
semilogy(N,error4_gl,'bo','LineWidth',2.0)
% hold on
% semilogy(N_mc,error4_mc,'ko','LineWidth',2.0)
xlabel('N')
ylabel('|l-l_n|')
legend('C-C','G-L','M-C')

subplot(3,2,5)
semilogy(N,error5_cc,'ro','LineWidth',2.0)
hold on
semilogy(N,error5_gl,'bo','LineWidth',2.0)
% hold on
% semilogy(N_mc,error5_mc,'ko','LineWidth',2.0)
xlabel('N')
ylabel('|l-l_n|')
legend('C-C','G-L','M-C')

subplot(3,2,6)
semilogy(N,error6_cc,'ro','LineWidth',2.0)
hold on
semilogy(N,error6_gl,'bo','LineWidth',2.0)
% hold on
% semilogy(N_mc,error6_mc,'ko','LineWidth',2.0)
xlabel('N')
ylabel('|l-l_n|')
