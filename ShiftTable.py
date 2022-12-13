#Fills the shift table used by Horspool’s and Boyer-Moore algorithms
#Input: Pattern P[0..m − 1] and an alphabet of possible characters
#Output: Table[0..size − 1] indexed by the alphabet’s characters and
# filled with shift sizes computed by formula
def ShiftTable(P):
    Table=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    size=len(Table)
    m = len(P)
    for i in range(0,size):
        Table[i]=m

    for j in range(0,m-1):
        index=ord(P[j])-ord('a')
        Table[index]=m-1-j
    print(Table)

P="barber"#6 azaltması gerektiğinde 0 yazmıyor 6 olarak bırakıyor

ShiftTable(P)
