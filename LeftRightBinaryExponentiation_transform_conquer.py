LeftRightBinaryExponentiation
#Computes an by the left-to-right binary exponentiation algorithm
#Input: A number a and a list b(n) of binary digits bI ,...,b0
# in the binary expansion of a positive integer n
#Output: The value of an
def LeftRightBinaryExponentiation(a,b):
    product =a
    n=len(b)

    I=n-2


    for i in range(1,n):
        product=product*product
        if b[i]==1:
            product=product*a
    return product

a=2
b=[1,1,0,1]
s=LeftRightBinaryExponentiation(a,b)
print(s)
