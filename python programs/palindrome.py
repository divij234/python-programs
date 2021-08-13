no=int(input("Enter a number : "))
temp=no
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
    
    
