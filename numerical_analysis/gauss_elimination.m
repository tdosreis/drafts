% Problem 4
%-------------------------------------------------------------------------%
clear all
close all
clc
%-------------------------------------------------------------------------%

f0='%8.0f %12.4e\n';

n = 11; 

N = 1000;

a = zeros(n,1); 

b = zeros(n-1,1); 

c = b;

i = (1:n)'; 

j = (1:N)';

x = (i-1)/(n-1);

% x = ((i-1)/(n-1)).^2;

f = exp(-x);

% f = sqrt(x).^5;

% f = 1./(1 + (x).^2);

dx = x(2:n)-x(1:n-1); 

df = (f(2:n)-f(1:n-1))./dx;

a(1) = 2; 

a(n) = 2; 

b(n-1) = 1;

c(1) = 1;

v(1) = 3*df(1); 

v(n) = 3*df(n-1);

a(2:n-1) = 2*(dx(1:n-2)+dx(2:n-1));

b(1:n-2) = dx(2:n-1); 

c(2:n-1) = dx(1:n-2);

v(2:n-1) = 3*(dx(2:n-1).*df(1:n-2)+dx(1:n-2).*df(2:n-1));

% Gauss elimination without pivoting (Tridiagonal)
%-------------------------------------------------%
y=zeros(n,1);

for i=2:n
    
    r=b(i-1)/a(i-1);
    
    a(i)=a(i)-r*c(i-1);
    
    v(i)=v(i)-r*v(i-1);
    
end

y(n)=v(n)/a(n);

for i=n-1:-1:1
    
    y(i)=(v(i)-c(i)*y(i+1))/a(i);
    
end

m = y;

c0=f(1:n-1); 
c1=m(1:n-1);
c3=(m(2:n)+m(1:n-1)-2*df)./(dx.^2);
c2=(df-m(1:n-1))./dx-c3.*dx;

emax=zeros(n-1,1);

for i=1:n-1
    
    xx = x(i) + ((j-1)/(N-1))*dx(i);
    
    t = xx - x(i);
    
    s = c3(i);
    
    s = t.*s+c2(i);
    
    s = t.*s+c1(i);
    
    s = t.*s+c0(i);
    
    emax(i) = max(abs(s-exp(-xx)));
    
%     emax(i)=max(abs(s-sqrt(xx).^5));
    
%     emax(i)=max(abs(s-1./(1 + (xx).^2)));
    
    fprintf(f0,i,emax(i))
    
end




