#Finds an optimal binary search tree by dynamic programming
#Input: An array P[1..n] of search probabilities for a sorted list of n keys
#Output: Average number of comparisons in successful searches in the
# optimal BST and table R of subtrees’ roots in the optimal BST
import math
from numpy import *
def OptimalBST(P):
    n=len(P)

    C = array(zeros((n+1,n+1)))
    R = array(zeros((n+1,n+1)))
    i=1
    while i<=n:

        C[i-1][i-1]=0

        C[i-1][i]=P[i-1]


        R[i-1][i]=i
        i=i+1
    C[n-1][n-2]=0

    d=1

    while d<=n-1:
        i=1

        while i<=n-d:

            j=i+d
            minval=math.inf

            k=i
            while k<=j:
                if C[i-1][k-1]+C[k][j]<minval:

                    minval=C[i-1][k-1]+C[k][j]

                    kmin=k-1

                k=k+1


            R[i-1][j]=kmin+1

            sum=P[i-1]
            s=i+1

            while s<=j:
                sum=sum+P[s-1]
                s=s+1
            C[i-1][j]=minval+sum

            i=i+1

        d=d+1


    return C[0][n],R#veya  return C,R
P=[0.1,0.2,0.4,0.3]
s=OptimalBST(P)
print(s)










