#bruteforce
a=[89, 45, 68, 90, 29, 34, 17]
n=len(a)
for i in range(0,n-1):
    for j in range(0,n-1-i):
        if a[j+1]<a[j]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
            print(a)
