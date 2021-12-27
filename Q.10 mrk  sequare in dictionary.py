# def dict():
#     n=int(input("Enter your number till where you want sequare:"))
#     i=1
#     sum=0
#     while i<=n:
#         sum=i*i
#         print(i,":",sum)
#         i=i+1
# dict()



def square():
    i=1
    d={}
    while i<=20:
        d.update({i:i*i})
        i=i+1
    print(d)
square()


# def square(a):
#     i=1
#     count=0
#     b=[]
#     f=[]
#     while i<=20:
#         if count<=5:
#             b.append(i*i)
#         # else:
#             # b.append(i*i)
#         count+1
#         i=i+1
#     f.append(b)
#     print(f)
# square(20)


