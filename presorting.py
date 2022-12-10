# PresortElementUniqueness(A[0..n − 1])
# Solves the element uniqueness problem by sorting the array first
# Input: An array A[0..n − 1] of orderable elements
# Output: Returns “true” if A has no equal elements, “false” otherwise sort the array A
def PresortElementUniqueness(A, n):
    for i in range(0, n - 2):
        if A[i] == A[i + 1]:
            return False
    return True


'''PresortMode(A[0..n − 1])
//Computes the mode of an array by sorting it first
//Input: An array A[0..n − 1] of orderable elements
//Output: The array’s mode
sort the array A'''


def PresortMode(A, n):
    i = 0
    modefrequency = 0
    while i <= n - 1:
        runlength = 0
        runvalue=A[i]
        while i+runlength <= n -1 and A[i+runlength]==runvalue:
            runlength=runlength+1
        if runlength > modefrequency:
            modefrequency=runlength
            modevalue=runvalue
        i=i+runlength
    return runvalue
A=[]
n=len(A)
s=PresortMode(A,n)
b=PresortElementUniqueness(A,n)
print(s)
print(b)

