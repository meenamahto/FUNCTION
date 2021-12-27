def sum(n):
    t=0
    i=0
    while i<len(n):
        t+=n[i]
        i=i+1
    print(t)
sum((8,2,3,0,7))

def mul(n):
    i=0
    t=1
    while i<len(n):
        t*=n[i]
        i=i+1
    print(t)
mul((8, 2, 3, -1, 7))