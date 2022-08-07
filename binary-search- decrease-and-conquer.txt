"""
 BinarySearch(A[0..n − 1], K)
//Implements nonrecursive binary search
//Input: An array A[0..n − 1] sorted in ascending order and
// a search key K
//Output: An index of the array’s element that is equal to K
// or −1 if there is no such element
"""
def binarysearch():
    A = [3,14,27,31,39,42,55,70,74,84,85,93,98]
    n = len(A)
    K = int(input("aranan değer"))
    l=0
    r=n-1
    while l<=r:
        m=int((l+r)/2)
        if K==A[m]:
            return m
        elif K<A[m]:
            r=m-1
        else:
            l=m+1
    return -1



b=binarysearch()
print(b)
