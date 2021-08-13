hardness=input("Enter the hardness : ")
cc=input("Enter the Carbon content : ")
ts=input("Enter the Tensile strength")
if(hardness>50 and cc<0.7 and ts>5600):
    print("Grade is 10")
    else if(hardness>50 and cc<0.7):
        print("Grade is 9")
        else if(cc<0.7 and ts>5600):
            print("Grade is 8")
            else if (hardness>50 and ts>5600):
            print("Grade is 7")

            else if (hardness>50 or cc<0.7 or ts< 5600):
            print ("Grade is 6")
            else:
                print("Grade is 5")
                  
