no=int(input("Enter a number : "))
temp=no
sum=0
while temp !=0:
    a=temp%10
    sum=sum+a**3
    temp=temp//10

if sum==no:
    print("It is an Armstrong number")
else:
    print("It is not an armstrong number")
