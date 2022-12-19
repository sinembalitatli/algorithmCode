#ComparisonCountingSort(A[0..n − 1])
#Sorts an array by comparison counting
#Input: An array A[0..n − 1] of orderable elements
#Output: Array S[0..n − 1] of A’s elements sorted in nondecreasing order
def ComparisonCountingSort(A, n):
    count = list()
    S = list()  # önceden boyutunu bilinen  boş listeler oluşturmak  için çözüm olabilir
    for j in range(1, n + 1):
        count.append(0)
    for a in range(1, n + 1):
        S.append(0)

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
ComparisonCountingSort(A,n)
