def rev(n):
    b=list(n)
    i=0
    while i<len(b):
        c=b[::-1]
        i=i+1
    d="".join(c)
    print(d)
rev("1234abcd")