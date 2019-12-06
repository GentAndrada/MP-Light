n = 0:199;
x=input('Enter x as a function of n: ');

for n=1:200
if n==1
    y(n) = -1.5.*x(n)+2.*x(n+1) - 0.5.*x(n+2);
elseif n>1 && n<199
    y(n) = 0.5.*x(n+1)-0.5.*x(n-1);
elseif n==200
    y(n) = 1.5.*x(n)-2.*x(n-1)+0.5.*x(n-2);
else 
    y(n) = NaN;
end
end

plot(x);
hold on
plot(y,'r');
xlabel 'x-axis'
ylabel 'y-axis'
title 'Machine Problem 5'
legend('x(n)','y(n)')