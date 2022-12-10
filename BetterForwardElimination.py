''' BetterForwardElimination(A[1..n, 1..n], b[1..n])
//Implements Gaussian elimination with partial pivoting
//Input: Matrix A[1..n, 1..n] and column-vector b[1..n]
//Output: An equivalent upper-triangular matrix in place of A and the
//corresponding right-hand side values in place of the (n + 1)st column'''
import numpy as np
def BetterForwardElimination(A,b,n):
    for i in range(1,n):
        A[i,n+1]=b[i]
    for i in range(1,n-1):
        pivotrow=i
        for j in range(j+1,n):
            if abs(A[j,i])>abs(A[pivotrow,i]):
                pivotrow=j
        for k in range(i,n+1):
            temp=A[i,k]
            A[i,k]=A[pivotrow,k]
            A[pivotrow,k]=temp
        for j in range(i+1,n):
            temp2=A[j,i]/A[i,i]
            for k in range(i,n+1):
                A[j,k]=A[j,k]-A[i,k]*temp2

A=np.array([[2,-1,1],[4,1,-1],[1,1,1]])
b=np.array([[1,5,0]])
n=len(A[:1])
s=BetterForwardElimination(A,b,n)
print(s)



