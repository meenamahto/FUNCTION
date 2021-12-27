def n(num):
    if num%10!=0:
        print(num)
    else:
        n(num=num//10)
k=(int(input("Enter your number:")))
n(k)