# add=lambda x,y:(x+y,x*y)
# a,b=(add(2,3))
# print(a)
# print(b)


# mod=lambda a,b=5:a*b
# print(mod(5))

a=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
a.sort(key=lambda x:x[1])
print(a)

