def vote(v):
    if v<18:
        print("not eligible:")
    else:
        print("eligible for vote")
a=int(input("Enter your age :"))
vote(a)


#without aarguments-

def oddeven():
    n=int(input("Enter your number:"))
    i=1
    while i<=n:
        if i%2==0:
            print("even",i)
        else:
            print("odd",i)
        i=i+1
oddeven()