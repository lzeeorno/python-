#guessing game
import random

#set traget randomly
target = random.randrange(1,20)

#set the max number of guesses
guess_time = 0

while True:
    guess_time+=1
    if guess_time >3:
        print("You are run out of guesses. The correct number was "+str(target)+'.')
        break

    try:
        guess =int(input("Enter a guess (1-20): "))

    except ValueError:
        print("Not a number!")
        guess_time-=1
        continue

    if (guess<1 or guess>20):
        print("please select number between 1 and 20!")
        guess_time-=1
        continue

    #game
    if(guess > target):
        print('Too high!')
    elif(guess < target):
        print("Too low!")
    else:
        print('correct, the answer is '+str(guess)+'.')
        break
