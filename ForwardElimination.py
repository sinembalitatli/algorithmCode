''' ForwardElimination(A[1..n, 1..n], b[1..n])
//Applies Gaussian elimination to matrix A of a system’s coefficients,
//augmented with vector b of the system’s right-hand side values
//Input: Matrix A[1..n, 1..n] and column-vector b[1..n]
//Output: An equivalent upper-triangular matrix in place of A with the
//corresponding right-hand side values in the (n + 1)st column '''



import numpy as np
def ForwardElimination(A,b,n):
    for i in range(1,n):
        A[i+1]=b[i]
    for i in range(1,n-1):
        for j in range(i,n):
            for k in range(i,n+1):
                A[j,k]=A[j,k] - A[i,k]*A[j,i]/A[i,i]
A=np.array([[2,-1,1],[4,1,-1],[1,1,1]])
b=np.array([[1,5,0]]).T
n=len(A[1:])
s=ForwardElimination(A,b,n)
print(s)
