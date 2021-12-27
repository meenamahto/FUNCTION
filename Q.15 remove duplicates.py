def duplicate(n):
    i=0
    b=[]
    while i<len(n):
        if n[i] not in b:
            b.append(n[i])
        i=i+1
    print(b)
duplicate([1,2,3,3,3,3,4,5])