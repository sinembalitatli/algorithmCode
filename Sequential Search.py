#bruteforce
def sequentialsearch():
    a=[89, 45, 68, 90, 29, 34, 17]
    n = len(a)
    K=int(input("enter key"))
    i = 0
    while a[i] != K:
        i = i + 1
    if i < n:
        return i

    else:
       return -1
   
s=sequentialsearch()
print(s)
#bulunmayan değer için hata veriyor
