print("BMI Calculator")
print("")
print("1. Weight in pounds, height in inches.")
print("2. Weight in kilograms, height in meters.")
print("")
userInput = input("Choice between 1 and 2?: ")
print("")
if userInput == '1':
    weight = int(input("Weight in pounds?: "))
    height = float(input("Height in inches?: "))
    bmi = (weight*703)/(height*height)
    print("")
    print("Result....")
    print("")
    print("Weight:     ",weight, "pounds")
    print("Height:     ",height, "inches")
    print("BMI:        ",round(bmi,1))
    if bmi < 18.5:
        print("Status:      Underweight")
    elif bmi > 18.5 and bmi < 25:
        print("Status:      Normal")
    elif bmi > 25 and bmi < 30:
        print("Status:      Overweight")
    elif bmi > 30:
        print("Status:    Obese")
    else:
        print("Your input may have an error!")
elif userInput == '2':
    weight = int(input("Weight in kilograms?: "))
    height = float(input("Height in meters?: "))
    bmi = weight/(height*height)
    print("")
    print("Result....")
    print("")
    print("Weight:     ",weight, "kilograms")
    print("Height:     ",height, "meters")
    print("BMI:        ",round(bmi,1))
    if bmi < 18.5:
        print("Status:      Underweight")
    elif bmi > 18.5 and bmi < 25:
        print("Status:      Normal")
    elif bmi > 25 and bmi < 30:
        print("Status:      Overweight")
    elif bmi > 30:
        print("Status:    Obese")
    else:
        print("Your input may have an error!")

          

                  



