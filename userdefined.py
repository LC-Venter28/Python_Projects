def square(val):
    result = val*val
    return result

valFromUser =int(input("Please enter a value to be squared: "))
valueFromFunction = square(valFromUser)

print("The result of the square is: ", valueFromFunction)
print("The result of the square is: ", square(valFromUser))#Nested statement
            
