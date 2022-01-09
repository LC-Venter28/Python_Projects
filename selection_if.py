mark=float(input("Please enter your mark: "))
year=int(input("Enter your Academic Year: "))

if mark<50 and year==1:
    print("Fail, qualify for supplementary exame")
elif mark<50 and year>1:
    print("Fail, no sup available")
elif mark >= 75:
    print("Distinction")
else:
    print("Pass")
