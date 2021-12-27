def oddeven(v):
    i=1
    while i<=v:
        if i%2==0:
            print("even=",i)
        else:
            print("odd=",i)
        i=i+1
a=int(input("Enter your number:"))
oddeven(a)
