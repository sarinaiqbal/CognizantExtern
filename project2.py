'''
Author: Sarina Iqbal
Python Project: Number Guessing Game
'''

import random
number_to_guess = random.randint(1,100)

count = 0 # Keep track of number of user attempts

while count < 10: # Loop runs 10 times
    user_guess = int(input("Guess a number between 1 and 100: "))
    count += 1 # Increment count
    if user_guess > number_to_guess: # High guess
        print("Too high! Try again.")

    elif user_guess < number_to_guess: # Low guess
        print("Too low! Try again.")

    else: # Correct guess
        print("Congratulations! You guessed it in", count, "attempts!")
        break # break out of loop when correct answer is guessed

# If count == 10 and guess is still incorrect, end game with a message   
if user_guess != number_to_guess:
    print("Game over! Better luck next time!")

