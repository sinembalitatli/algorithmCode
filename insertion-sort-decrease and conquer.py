#ALGORITHM InsertionSort(A[0..n − 1])
#Sorts a given array by insertion sort
#Input: An array A[0..n − 1] of n orderable elements
#Output: Array A[0..n − 1] sorted in nondecreasing order
#89,45,68,90,29,34,17 değerleri için doğrulandı

def insertiosort(A,n):
    for i in range(1,len(A)):
        v=A[i]
        j=i-1
        while j>=0 and A[j]>v:
            A[j+1]=A[j]
            j=j-1
        A[j+1]=v
    a=print(A)
A=[]
A.append(89)
A.append(45)
A.append(68)
A.append(90)
A.append(29)
A.append(34)
A.append(17)
n=len(A)
insertiosort(A,n)
