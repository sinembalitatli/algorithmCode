#Applies dynamic programming to find the minimum number of coins
#of denominations d1< d2 < . . . < dm where d1 = 1 that add up to a
#given amount n
#Input: Positive integer n and array D[1..m] of increasing positive
# integers indicating the coin denominations where D[1]= 1
#Output: The minimum number of coins that add up to n
import math
from numpy import *

def ChangeMaking(n,D):


    m=len(D)
    F =array(zeros((n+1)))


    F[0]=0
    i=1
    while i<=n:



        temp = math.inf
        j=1
        while j<=m and i>=D[j-1]:




            temp=min(F[i-D[j-1]],temp)

            j=j+1

        F[i]=temp+1

        i=i+1
    return F[n]

n=6
D=[1,3,4]
s=ChangeMaking(n,D)
print(s)


