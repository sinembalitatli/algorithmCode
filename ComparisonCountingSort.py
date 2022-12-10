#ComparisonCountingSort(A[0..n − 1])
#Sorts an array by comparison counting
#Input: An array A[0..n − 1] of orderable elements
#Output: Array S[0..n − 1] of A’s elements sorted in nondecreasing order
def ComparisonCountingSort(A, n,count,S):

    for i in range(0, n):
        count[i] = 0
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if A[i] < A[j]:
                count[j] = count[j] + 1
            else:
                count[i] = count[i] + 1
    for i in range(0, n):
        S[count[i]] = A[i]
    print(S)


A = [19, 31, 47, 62, 84, 96]
n = len(A)
count=[0,0,0,0,0,0]#liste boş boş olunca ininci eleman diye birşey olmuyor hata veriyor şimdilik geçiçci çözüm için
S=[0,0,0,0,0,0]#
ComparisonCountingSort(A, n,count,S)
