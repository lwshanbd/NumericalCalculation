%LU
clear
X = [4,-1,1;4,-8,1;-2,1,5];
Y = [7;-21;15];
L = eye(size(X));
U = X;
n=3;
m = zeros(n,n); % initial the n*n matrix m zeros 
for j = 1 : n-1
if abs(X(j,j))<eps 
error('zero pivot encountered'); 
end
for i = j+1 : n
L(i,j) = U(i,j)/U(j,j);
for k = j:n
U(i,k) = U(i,k) - L(i,j)*U(j,k);
end
end
end
 
