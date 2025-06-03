'''
Author: Sarina Iqbal
Python Project: Number
'''

import random
number_to_guess = random.randint(1,100)
print(number_to_guess)

user_guess = 0
count = 0

'''while count<(11) :
    while user_guess != number_to_guess:
        user_guess = int(input("Guess a number between 1 and 100: "))
        if user_guess > number_to_guess:
            print("Too high! Try again.")

        elif user_guess < number_to_guess:
            print("Too low! Try again.")
        count+=1
    break
print("Game over! Better luck next time!")

print("Congratulations! You guessed it in", count, "attempts!")'''


while count < 11:
    user_guess = int(input("Guess a number between 1 and 100: "))
    if user_guess > number_to_guess:
        print("Too high! Try again.")
        count+=1
    elif user_guess < number_to_guess:
        print("Too low! Try again.")
        count += 1
    else:
        print("Congratulations! You guessed it in", count, "attempts!")
        break
if user_guess != number_to_guess:
    print("Game over! Better luck next time!")

