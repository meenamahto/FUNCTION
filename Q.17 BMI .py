def bmi():
    w=float(input("Enter your weight here:"))
    h=float(input("Enter your hight here:"))
    b=0.3048
    c=1
    a=0
    while c<=h:
        a=a+b
        c=c+1
    # print(a)
    d=w/(a*a)
    if d<=18.0:
        print("underweight",d)
        print("need weight",18-d)
    elif d<=25.0:
        print("normal",d)
    elif d<=30.0:
        print("overweight",d)
        print("extra weight",30-d)
    else:
        print("obese",d)
        print("extra weight",d-30)
bmi()


