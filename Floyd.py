#Implements Floyd’s algorithm for the all-pairs shortest-paths problem
#Input: The weight matrix W of a graph with no negative-length cycle
#Output: The distance matrix of the shortest paths’ lengths
#D ←W //is not necessary if W can be overwritten
import math

from numpy import *
INF=999
def Floyd(W):
    n = len(W)

    D = array(zeros((n , n )))
    D=W
    k=1
    while k<n+1:
        i=1
        while i<n+1:
            j=1
            while j<n+1:


                D[i-1][j-1]=min(D[i-1][j-1],(D[i-1][k-1]+D[k-1][j-1]))
                j=j+1
            i=i+1
        k=k+1
    return D

W= [[0, INF,3 , INF],
         [2, 0, INF, INF],
         [INF, 7, 0,   1],
         [6, INF, INF, 0]
         ]
c=Floyd(W)
print(c)