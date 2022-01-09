import random
print("Type stop to stop loop")
userInput = input("Type roll to roll the dice!\n")

if userInput == 'roll':
    roll = random.randint(1,6)
    print("You rolled: ", roll)
elif userInput == "":
    print("Exit")
print("")
while userInput == 'roll':
    userInput = input("Type roll to roll the dice!\n")

    if userInput == 'roll':
        roll = random.randint(1,6)
        print("You rolled: ", roll)
    elif userInput == 'stop':
        print("Stopped")
    print("")

