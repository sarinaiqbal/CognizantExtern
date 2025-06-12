'''
Author: Sarina Iqbal
Python Assignment 6 Task 3
'''

while True: # loop to keep asking for numbers in case of error

    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        div = (num1/num2) # attempt division of num1 by num2
    except ValueError: # Error if non-numeric input is entered
        print("Invalid input. Please enter two valid numbers.")
    except ZeroDivisionError: # Error if num2 is 0
        print("Error, you cannot divide by zero.")
    else:
        # display the result if no exceptions occur
        # round result to 2 decimal places
        print(f"The result is {div:.2f}.")
        break # No errors, end loop
    finally:
        print("This block always executes.") # print a closing message regardless of exceptions