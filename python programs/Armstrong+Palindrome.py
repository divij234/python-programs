no=int(input("Enter a number : "))
new=int(input("Enter 1 to find if its palindrome or enter 2 to find if its armstrong"))

temp=no
if new==1:
    rev=0
    while temp !=0:
        d=temp%10
        rev=rev*10+d
        temp=temp//10
    print(rev)
    if rev==no:
        print("Palindrome")
    else:
        print("Not a Palindrome")
elif new==2:
    sum=0
    while temp !=0:
        a=temp%10
        sum=sum+a**3
        temp=temp//10

    if sum==no:
        print("It is an Armstrong number")
    else:
        print("It is not an armstrong number")
else:
    print("error")
