def chech(a):
    i=0
    l=0
    u=0
    while i<len(a):
        if a[i].isupper():
            u=u+1
        elif a[i].islower():
            l=l+1
        i=i+1
    print("upper letters=",u)
    print("lower letters=",l)
chech('The quick Brow Fox')