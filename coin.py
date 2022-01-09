import random

user = None

computer = random.choice([True,False])

while user == flip:
    user = input("Please enter flip to flip the coin:")
    flip = random.choice([True,False])
    if flip == True:
        print("Heads")
    elif flip == False:
        print("Tails")

