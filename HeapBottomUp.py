# HeapBottomUp(H[1..n])
#Constructs a heap from elements of a given array
# by the bottom-up algorithm
#Input: An array H[1..n] of orderable items
#Output: A heap H[1..n]

def  HeapBottomUp(H):

    n=len(H)
    a=int(n/2)
    for i in range(a,1):#aralıkları doğrula
        k=i
        v=H[k]
        heap=False
        while not heap and 2*k<=n:
            j=2*k
            if j<n:#there are two children
                if H[j]<H[j+1]:
                    j=j+1
            if v>=H[j]:
                heap=True
            else:
                H[k]=H[j]
                k=j
        H[k]=v
        print(H)

H = [8, 7, 5, 6, 9, 82]
HeapBottomUp(H)
#hatasız çalışıyor ama çıktı none


