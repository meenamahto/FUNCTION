def calculator(num1,num2,operator):
    if operator=="+":
        print(num1+num2)
    elif operator=="-":
        print(num1-num2)
    elif operator=="*":
        print(num1*num2)
    elif operator=="/":
        print(num1/num2)
a=int(input("Enter your number:"))
b=int(input("Enter your number:"))
c=input("Enter your operator:")
calculator(a,b,c)
