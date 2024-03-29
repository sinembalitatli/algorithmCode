
Horner(P[0..n], x)
#Evaluates a polynomial at a given point by Horner’s rule
#Input: An array P[0..n] of coefficients of a polynomial of degree n,
#stored from the lowest to the highest and a number x
#Output: The value of the polynomial at x


def Horner(P, x):
    b = []
    a = n - 2
    while not a < 0:
        b.append(a)
        a -= 1

    p = P[n - 1]
    for i in b:
        
        p = (x * p) + P[i]

    return p


P = [-5, 1, 3, -1, 2]
x = 3
n = len(P)

s = Horner(P,x)
print(s)
