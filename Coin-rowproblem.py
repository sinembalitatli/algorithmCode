# Applies formula (8.3) bottom up to find the maximum amount of money
# that can be picked up from a coin row without picking two adjacent coins
# Input: Array C[1..n] of positive integers indicating the coin values
# Output: The maximum amount of money that can be picked up
def CoinRow(n,C):

    F = list()  # önceden boyutunu bilinmeyen ama boyutuna ihtiaycı olunan boş listeler için çözüm olabilir

    for a in range(1, n + 1):
        F.append(0)

    F[0] = 0
    F[1] = C[0]

    i = 2
    while i <n:
        F[i] = max(C[i] + F[i - 2], F[i - 1])
       
        i = i + 1

    print(F[n - 1])
C=[5,1,2,10,6,2]
CoinRow(6,C)
