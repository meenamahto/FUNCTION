def range_function(min,max,step):
    i=min
    b=[]
    while i<=max:
        b.append(i)
        i=i+step
    print(b)
a=int(input("Enter your start value:"))
b=int(input("Enter your end number:"))
c=int(input("Enter your step value"))
range_function(a,b,c)
