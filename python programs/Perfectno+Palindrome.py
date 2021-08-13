num=int(input("Enter a number : "))
val=int(input("Enter 1 to see the factors of the number or enter 2 to see if it is a palindrome or not : "))

sum1=0
if val==1:
   for i in range(1,num):
       if(num % i == 0):
        sum1 = sum1 + i
   if (sum1==num):
       print("The number is a Perfect number!")
   else:
       print("The number is not a Perfect number!")
elif val==2:
    a=num
    rev=0
    while a !=0:
        d=a%10
        rev=rev*10+d
        a=a//10
    if rev==num:
        print("It is a palindrome number")
    else:
        print("It is not a palindrome number")
else:
    print("error")
        
    
