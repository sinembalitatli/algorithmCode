def russian_peasant_multiplication():
    n=int(input("n sayısını gir"))
    m=int(input("m sayısını gir"))
    result=0
    result1=0
    if n%2==0:
        while n!=1:
            n=n//2
            m=2*m

            if n%2!=0 and n!=1:

                result1=result1+m
    result=(m*n)+result1
    print(result)



russian_peasant_multiplication()
