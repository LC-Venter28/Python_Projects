print("Question 1")
print("")
numstart=1

userInput = int(input("Enter the number of values to display: "))

while numstart <= userInput :
    print(numstart)
    numstart += 1
print("")
print("")
print("Question 2")
print("")
print("Enter some numbers to calculate the sum.")
print("Enter a negative value to see the Sum of all values")
print("")
total = 0
number = 1
while number > 0:
    number = float(input("Enter value number: "))
    if number > 0:
        total = total + number
print("The sum of the numbers is", total)
print("")
print("")
print("Question 3")
print("")
n = int(input("Enter number of terms to be completed: "))
print("Fibonacci series")
f = 0
s = 1
for i in range(n):
    print(f)
    temp = f
    f = s
    s = temp+s
