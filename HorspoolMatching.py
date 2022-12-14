#Implements Horspool’s algorithm for string matching
#Input: Pattern P[0..m − 1] and text T [0..n − 1]
#Output: The index of the left end of the first matching substring
# or −1 if there are no matches
#ShiftTable(P [0..m − 1]) //generate Table of shifts






def ShiftTable(Table,P):#ilk atanan m değerikadar  azaltması gerektiğinde 0 yazmıyor m olarak bırakıyor

    size=len(Table)
    m = len(P)
    for i in range(0,size):
        Table[i]=m

    for j in range(0,m-1):
        index = ord(P[j]) - ord('a')
        Table[index] = m - 1 - j



def HorspoolMatching(T,P):
    Table = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z']

    n = len(T)
    m = len(P)
    ShiftTable(Table,P)
    i=m-1
    while i<=n-1:
        k=0
        while k<=m-1 and P[m-1-k]==T[i-k]:
            k += 1
        if k==m:
            x=i - m + 1
            return x

        else:
            index2 = ord(T[i]) - ord('a')
            i=i+Table[index2]

    return -1






T=list("abaaabcd")
P=list("abc")
s=HorspoolMatching(T,P)
print(s)
