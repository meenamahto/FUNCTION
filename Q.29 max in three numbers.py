
# def max(a,b):
#     if a>b:
#         return a
#     return b
# def final_max(a,b,c):
#     return max(a,max(b,c))
# print(final_max(3,2,4))


def max(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    return c
x=max(9,1,5)
print(x)



