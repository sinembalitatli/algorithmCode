#bruteforce
import math


# uzaklık veriyor
def BruteForceClosestPair():
    # sınırlar  kesin doğrulanmalı
    listx = []
    listy = []
    distances = []

    while True:
        a = int(input("x noktasının  0'a olan uzaklıklarını gir"))
        if a == -1:
            break
        listx.append(a)

    while True:
        b = int(input("y noktasının 0'a olan uzaklıklarını gir "))
        if b == -1:
            break
        listy.append(b)

    n = len(listx)

    for i in range(0, n - 1):
        print(i)

        for j in range(i + 1, n):
            xj = listx[j]
            xi = listx[i]
            yi = listy[i]

            yj = listy[j]
            sx = (xi - xj) ** 2
            sy = (yi - yj) ** 2
            s = sx + sy
            d = math.sqrt(s)
            distances.append(d)
            dmin = min(distances)
    return dmin
s=BruteForceClosestPair()
print(s)#sadece çıktıyı göstermiyor


































