from numpy import *
def MFKnapsack(i,j,Weights,Values):

    F =array(zeros((i+1,j+1)))

    if(i==0 or j==0):
        return 0
    if j < Weights[i - 1]:
        value=MFKnapsack(i-1,j,Weights,Values)
    else:
        value=max(MFKnapsack(i-1,j,Weights,Values),Values[i-1]+MFKnapsack(i-1,j-Weights[i-1],Weights,Values))
    F[i][j]=value
    return F[i][j]



j=5
Weights=[2,1,3,2]
Values=[12,10,20,15]
i=len(Values)
s=MFKnapsack(i,j,Weights,Values)
print(s)


#knapsack brute force algoritması örneğindeki girdi değerleri  için denendi
#j=10
#Weights=[0,7,3,4,5,10,11,12,7,8,9,14,15,16,12,19]
#Values=[0,42,12,40,25,54,None,None,52,37,65,None,None,None,None,None]
#i=len(Values)
#s=MFKnapsack(i,j,Weights,Values)
#print(s)
