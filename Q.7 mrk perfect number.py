# def perfect_number():
#     n=int(input("Enter your number:"))
#     i=1
#     sum=0
#     while i<n:
#         if n%i==0:
#             sum=sum+i
#         i=i+1
#     if sum==n:
#         print("perfect number=",sum)
#     else:
#         print("not perfect number=",sum)
# perfect_number()




# def perfect():
#     n=1
#     b=[]
#     while n<=1000:
#         i=1
#         sum=0
#         while i<n:
#             if n%i==0:
#                 sum=sum+i
#             i=i+1
#         if sum==n:
#             b.append(sum)
#         n=n+1
#     print(b)
# perfect()    



# prime number
n=1
b=[]
while n<=100:
    i=1
    # b=[]
    count=0
    while i<=n:
        if n%i==0:
            count+=1
        i=i+1
    if count==2:
        b.append(n)
    n=n+1
print(b)
