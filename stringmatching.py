#bruteforce
t="nobodynoticedhim"
p="not"
m = len(p)
n = len(t)
for i in range(0, n - m):
        j = 0
        while j < m and p[j] == t[i + j]:
            j= j + 1
            if j == m:
               print(i)
            else:
                print("-1")

#return şeklinde değil,eşleşme olduğu zamana kadar ki kısımda -1 döndürüyor
