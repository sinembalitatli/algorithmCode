#bruteforce
a = [89, 45, 68, 90, 29, 34, 17]
n = len(a)
for i in range(0, n - 1):
  enkucuk = i
  for j in range(i + 1, n):
    if a[j] < a[enkucuk]:
      enkucuk = j

  temp = a[i]
  a[i] = a[enkucuk]
  a[enkucuk] = temp
  print(a)
