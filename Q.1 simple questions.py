
# def check(a):
#     i=0
#     while i<len(a):
#         j=0
#         while j<len(a[i]):
#             if a[i][0]==a[i][-1]:
#                 print("true")
#                 break
#             else:
#                 print("false")
#                 break
#             j=j+1           
#         i=i+1
#         break
# b=['abca', 'xyzx', 'aba', '1221']
# check(b)



# a=[1,2,3,4,5,6,7,8,0,9,3,4]
# i=0
# b=[]
# n=[]
# count=0
# while i<len(a):
#     if count==5:
#         n.append(b)
#         b=[]
#     else:
#         b.append(a[i])
#     count+=1
#     i=i+1
# n.append(b)
# print(n)



# a=[2,5,4,3,1,8,9,3]
# i=0
# # c=0
# def sort(a):
#     i=0
#     c=0
#     while i<len(a):
#         j=0
#         while j<len(a)-1:
#             c=a[j]
#             a[j]=a[j+1]
#             a[j+1]=c
#         j=j+1
#     i=i+1
#     print(a)
# b= [6, 8, 4, 3, 9, 56, 0, 34, 7, 15]
# sort(b)

# while i<len(a):
#     j=0
#     while j<len(a)-1:
#         if a[j]>a[j+1]:
#             c=a[j]
#             a[j]=a[j+1]
#             a[j+1]=c
#         j=j+1
#     i=i+1
# print(a)

# def func(a):
#     # c=0
#     for i in range(len(a)):
#         for j in range(len(a)-1):
#             if a[j]>a[j+1]:
#                 c=a[j]
#                 a[j]=a[j+1]
#                 a[j+1]=c
#     print(a)
# a= [6, 8, 4, 3, 90, 56, 0, 34, 7, 15]
# func(a)






# def perfect_number():
#     n=1
#     while n<=1000:
#         i=1
#         sum=0
#         while i<n:
#             if n%i==0:
#                 sum+=i
#             i=i+1
#         if sum==n:
#             print(sum)
#         n=n+1

   
# perfect_number()



# def max_of_two( x, y ):
#     if x > y:
#         return x
#     return y
# def max_of_three( x, y, z ):
#     return max_of_two( x, max_of_two( y, z ) )
# print(max_of_three(10, 6, 8))

# a="1234abcd"









# def sort(n):
#     i=0
#     while i<len(n):
#         j=0
#         while j<len(n)-1:
#             if n[j]>n[j+1]:
#                 c=n[j]
#                 n[j]=n[j+1]
#                 n[j+1]=c
#             j=j+1
#         i=i+1
#     print(n)
# sort([2,4,5,6,7,6,5,78,89,90,54,33,2])





# def a(n):
#     n=34
# def b(n):
#     n[0]=10
# d=12
# c=[12,13]
# a(d)
# b(c)
# print(d)
# print(c)


# def fun(**b):
#     d=b[a]+b[c]
#     return d
# fun(a=4,c=4)
