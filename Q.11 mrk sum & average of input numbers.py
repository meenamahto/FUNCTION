def sumavr():
    n=int(input("Enter your number of size:"))
    i=1
    sum=0
    while i<=n:
        a=int(input("Enter your number:"))
        sum=sum+a
        i=i+1
    print("sum=",sum)
    print("average=",sum//n)
sumavr()