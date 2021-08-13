principal=int(input("Enter the principal amount : "))
rate=int(input("Enter the rate of interest"))
time=int(input("Enter the term of loan"))
CP=principal*[(1+rate/100)**time-1]
print("The Compound Interest is :",end=" ")
print(CP)
