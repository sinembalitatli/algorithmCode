from numpy import *
def RobotCoinCollection(C):
    n=len(C)

    m=n


    F = array(zeros((n,m+1)))

    F[1][1]=C[1][1]
    j=2
    while j<=m+1:

        F[0][j-1]=F[0][j-2]+C[0][j-1]

        j=j+1

    i=2
    while i<=n:
        F[i-1][0]=F[i-2][0]+C[i-1][0]

        i=i+1
        j = 2

        while j <= m+1:
            F[i-2][j-1] = max(F[i - 3][j-1], F[i-2][j - 2]) + C[i-2][j-1]

            j = j + 1


    return F[n-1,m]#veya return F

C=array([[0,0,0,0,1,0],[0,1,0,1,0,0],[0,0,0,1,0,1],[0,0,1,0,0,1],[1,0,0,0,1,0]])


s=RobotCoinCollection(C)

print(s)






