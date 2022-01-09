print("Question 1")
print("")
print("Enter 0 as the base to stop loop.")
print("")
userNum = input("Enter value to convert to decimal: ")
userBase = int(input("Enter the base of the value: "))
if userBase ==2:
    print(userNum,"in base",userBase,"=",int(userNum, 2),"in decimal")
if userBase ==8:
    print(userNum,"in base",userBase,"=",int(userNum, 8),"in decimal")
if userBase ==16:
    print(userNum,"in base",userBase,"=",int(userNum, 16),"in decimal")
print("")
while userBase > 0:
    userNum = input("Enter value to convert to decimal: ")
    userBase = int(input("Enter the base of the value: "))
    if userBase ==2:
        print(userNum,"in base",userBase,"=",int(userNum, 2),"in decimal")
    if userBase ==8:
        print(userNum,"in base",userBase,"=",int(userNum, 8),"in decimal")
    if userBase ==16:
        print(userNum,"in base",userBase,"=",int(userNum, 16),"in decimal")
    print("")
else:
    print("You chose to stop the loop!")
print("")
print("____________________________________________________________________________")
print("Question 2")
print("")
userInput = input(("Enter the word to test for palindrome: "))
reverse = userInput[::-1]
print("")
for i in range(len(userInput)):
    print (userInput[i], "--", reverse[i])
    if userInput[i].lower() != reverse[i].lower():
        print("")
        print("-->Not Palindrome")
        break
        
else:
    print("")
    print("-->Palindrome")

                  
