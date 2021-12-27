def string(a,b):
    if len(a)>len(b):
        print(a)
    elif len(a)==len(b):
        print(a)
        print(b)
    else:
        print(b)
a=input("Enter your name:")
b=input("Enter your name:")
string(a,b)