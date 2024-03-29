# ImplementsWarshall’s algorithm for computing the transitive closure
# Input: The adjacency matrix A of a digraph with n vertices
# Output: The transitive closure of the digraph
import sys
from numpy import *



def Warshall(A):
    n = len(A)

    Rtemp = array(zeros((n, n)))

    Rtemp = A
    k = 1
    while k < n+1:
        i = 1
        while i < n+1:
            j = 1
            Rtemp0=A

            while j < n+1:

                Rtemp[i-1][j-1] = Rtemp0[i-1][j-1] or (Rtemp0[i-1][k-1] and Rtemp0[k-1][j-1])

                Rtemp0 = Rtemp

                j = j + 1

            i = i + 1
        k = k + 1

    return Rtemp


A =  [[0, 1,0 , 0],
         [0, 0, 0, 1],
         [0, 0, 0,   0],
         [1, 0, 1, 0]
         ]
s = Warshall(A)
print(s)
