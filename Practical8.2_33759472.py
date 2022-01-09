print("Question 1")
print("")
userInput = int(input("Enter the number of values to display: "))
for i in range(1,userInput + 1):
    print(i)
print("")
print("")
print("Question 2")
print("")
print("Enter 0 as the base and exponent to break the loop")
print("")
base = int(input("Enter base value: "))
exp = int(input("Enter exponent value: "))
for index in range(1):
    print(base,"raised to the power of",exp,"=",pow(base,exp))
print("")
while base > 0:
    base = int(input("Enter base value: "))
    exp = int(input("Enter exponent value: "))
    for index in range(1):
        print(base,"raised to the power of",exp,"=",pow(base,exp))
    print("")
if base == 0:
    print("")
print("")
print("Question 3")
print("")
multi = int(input("Enter value for multiplication table: "))
for j in range(1,multi+1):
    for k in range(1,13):
        print(j * k, end='\t')
