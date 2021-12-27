def sort(a):
    i=0
    while i<len(a):
        j=0
        while j<len(a)-1:
            if a[j]>a[j+1]:
                c=a[j]
                a[j]=a[j+1]
                a[j+1]=c
            j=j+1
        i=i+1
    print(a)
sort([6, 8, 4, 3, 9, 56, 0, 34, 7, 15])


# def sum(a):
#     i=0
#     sum=0
#     while i<len(a):
#         sum+=a[i]
#         i=i+1
#     print(sum)
# sum([1, 2, 3, 4, 5])