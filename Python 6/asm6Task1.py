'''
Author: Sarina Iqbal
Python Assignment 6 Task 1
'''

while True: # loop to keep asking for number in case of error
    try:
        number = int(input("Enter a number: "))
        result = 100/number
    except ZeroDivisionError:
        print("Sorry, you cannot divide by zero.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    else: # if no errors, print result and break out of loop
        print(f"100 divided by {number} is {result:.2f}") # rounding result to 2 decimal places
        break
