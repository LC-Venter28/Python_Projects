
import random

guess_limit = None
user = None
start_num = None
end_num = None


while guess_limit == None:
    try:
        guess_limit = int(input('Please enter the number you want to try to guess:'))
        print('You have {} times to guess left'.format(guess_limit))
    except ValueError or guess_limit == 0:
        guess_limit = 1
        print('You only have one chance to guess')

while start_num == None and end_num == None:
    try:
        start_num = int(input('Enter the number you want to start:'))
        end_num = int(input('Enter the number you want to end:'))
        if start_num >= end_num:
            print('start num must be smaller than the end num')
            start_num = None
            end_num = None
    except ValueError:
        print('You must enter the int Value for the start and the end')
        start_num = None
        end_num = None


computer = random.randrange(start_num, end_num)
print(computer)

while user == None and guess_limit !=0 :
    try:
        user = int(input('Please enter the number you want to guess:'))
    except ValueError:
        print('You must enter the int value')
        user = None
    if user == computer:
        print('You win the game')
    elif user > computer:
        print('You guess the wrong number, too high')
        user = None
        guess_limit -= 1
    elif user < computer:
        print('You guess the wrong number, too low')
        user = None
        guess_limit -= 1

if guess_limit == 0:
    print('you lost the game')
