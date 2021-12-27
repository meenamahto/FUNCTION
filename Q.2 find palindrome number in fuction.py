def palindrome(v):
    rev=0
    while v>0:
        rev=rev*10+v%10
        v=v//10
        # print(rev)
    if rev==n:
        print("palindrome number:")
    else:
        print("not palindrome")
n=int(input("Enter your number:"))
palindrome(n)