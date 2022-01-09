bi = 2
Oct = 8
Hex = 16
print("")
print("Input a negative value as the base to stop the loop.")
print("")
usernum = int(input("Enter decimal number to convert to base: "))
base = int(input("Enter base for conversion: "))
print("    ___")
print(base,'|',usernum)
if base == 2:
    print("Base",base,"value of",usernum,"=",bin(usernum))
elif base == 8:
    print("Base",base,"value of",usernum,"=",oct(usernum))
elif base == 16:
    print("Base",base,"value of",usernum,"=",hex(usernum))
print("")
while base > 0:
    usernum = int(input("Enter decimal number to convert to base: "))
    base = int(input("Enter base for conversion: "))
    print("    ___")
    print(base,'|',usernum)
    if base == 2:
        print("Base",base,"value of",usernum,"=",bin(usernum))
    elif base == 8:
        print("Base",base,"value of",usernum,"=",oct(usernum))
    elif base == 16:
        print("Base",base,"value of",usernum,"=",hex(usernum))
    elif base < 0:
        print("Please enter a valid number!")
    print("")
