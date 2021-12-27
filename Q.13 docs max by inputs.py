def max():
    a=int(input("Enter your number:"))
    b=int(input("Enter your number:"))
    c=int(input("Enter your number:"))
    if a>b and a>c:
        print(a,"max")
    elif b>a and b>c:
        print(b,"max")
    else:
        print(c,"max")
max()