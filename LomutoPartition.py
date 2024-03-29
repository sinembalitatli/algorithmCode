//Partitions subarray by Lomuto’s algorithm using first element as pivot
//Input: A subarray A[l..r] of array A[0..n − 1], defined by its left and right
// indices l and r (l ≤ r)
//Output: Partition of A[l..r] and the new position of the pivot
def LomutoPartition():
    A = [ 10,7, 8, 9, 1, 5]
    l=0
    p=A[l]
    s=l

    r=len(A)

    for i in range(l+1,r):
        if A[i]<p:
            s = s + 1
            temp = A[s]
            A[s] = A[i]
            A[i] = temp

    temp2=A[l]
    A[l]=A[s]
    A[s]=temp2

    return s,A
a=LomutoPartition()
print(a)

