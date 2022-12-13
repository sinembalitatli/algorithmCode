#DistributionCountingSort(A[0..n − 1], l, u)
#Sorts an array of integers from a limited range by distribution counting
#Input: An array A[0..n − 1] of integers between l and u (l ≤ u)
#Output: Array S[0..n − 1] of A’s elements sorted in nondecreasing order
def DistributionCountingSort(A,n,D,S):

    #önceden eleman sayısı bilinen boş array oluşturma???
    lmin=min(A)
    umax=max(A)
    x=(umax-lmin)+1
    for i in range(0,n):
        D[A[i]-lmin]=D[A[i]-lmin] +1
    for j in range(1,x):
        D[j]=D[j-1]+D[j]
    c = []
    # python aralık mantığını değiştirmek için:)
    d = n - 1
    while not d < 0:  # sıfıra kadar geri sayma mantığı

        c.append(d)
        d -= 1



    for i in c:
        j=A[i]-lmin
        S[D[j]-1]=A[i]
        D[j]=D[j]-1
    print(S)
A=[13,11,12,13,12,12]
n=len(A)
D=[0,0,0,0,0,0]#iyileştirme yaparsak:frekansa bağlı boyutu değişiyor frekansını bulup  boyut ona bağlı oluşturma,yada direk eleman sayısı kadar oluşturursa garanti çalışır sadece bazı durumlarda gereksiz alan kullanımı
S=[0,0,0,0,0,0]
DistributionCountingSort(A,n,D,S)



