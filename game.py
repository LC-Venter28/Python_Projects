import random

print("RPG Game")
print("")
print("Class:")
print("")
print("1 for Rogue")
print("2 for Warrior")
print("3 for Mage")
print("")
userClass = int(input("Choose Class: "))
print("")
if userClass == 1:
    print("You chose Rogue!")
elif userClass == 2:
    print("You chose Warrior!")
elif userClass == 3:
    print("You chose Mage!")
else:
    print("Invalid Choice")
print("")
print("Your abilities are:")
print("")
agility = int(random.randint(0, 10))
strength = int(random.randint(0, 10))
intellect = int(random.randint(0, 10))
print("Agility: ", agility)
print("Strength: ", strength)
print("Intellect: ", intellect)
print("")
if userClass == 1:
    if agility >= 5:
        print("You were agile enough")
    else:
        print("You were'nt agile enough")
elif userClass == 2:
    if strength >= 5:
        print("You were strong enough")
    else:
        print("You were'nt strong enough")
elif userClass == 3:
    if intellect >= 5:
        print("You were smart enough")
    else:
        print("You were'nt smart enough")
