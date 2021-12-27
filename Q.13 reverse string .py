# def string():
#     a=input("Enter your string:")
#     str=''
#     i=len(a)
#     while i>0:
#         str+=a[i-1]
#         i-=1
#     print(str)
# string()



def string(a):
    str=''
    i=len(a)
    while i>0:
        str+=a[i-1]
        i-=1
    print(str)
string("1234abcd")
