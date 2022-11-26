#RightLeftBinaryExponentiation(a, b(n))
#Computes an by the right-to-left binary exponentiation algorithm
#Input: A number a and a list b(n) of binary digits bI ,...,b0
# in the binary expansion of a nonnegative integer n
#Output: The value of an

def  RightLeftBinaryExponentiation(a,b):
    n=len(b)
    c = []
    # python aralık mantığını değiştirmek için:)
    d = n -2
    while not d <0:  # 1 e kadar geri sayma mantığı
        c.append(d)
        d -= 1
    term = a
    if b[n - 1] == 1:
        product = a
    else:
        product = 1

    for i in c:
        term=term*term
        if b[i]==1:
            product=product*term
    return product
a=2
b=[1,1,0,1]
s=RightLeftBinaryExponentiation(a,b)
print(s)

