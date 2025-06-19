'''
Author: Sarina Iqbal
Python Project: Calculator with Exception Handling
Description: Simulates a calculator that carries out four mathematical operations
and handles exceptions gracefully, also logging those into a text file. 
'''

import logging 

# logging into file error_log.txt to enter errors
logging.basicConfig(filename="error_log.txt", level=logging.ERROR)
logger = logging.getLogger()

# displaying options and asking for choice at beginning 
choice = int(input('''Welcome to the Error-Free Calculator! 
Choose an operation: 
    1. Addition 
    2. Subtraction 
    3. Multiplication 
    4. Division 
    5. Exit
    Enter your choice (1/2/3/4/5)> '''))


while choice != 5: #continue asking until user wishes to exit
    if choice == 1: #addition
        try:
            # ask for inputs and try to add
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            add = num1 + num2
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            logger.error("ValueError occurred: invalid numeral.") #logging ValueError to file
        else:
            # If operation passes with no errors, print result
            print(f"The summation is = {add}.")

    if choice == 2: # subtraction
        try:
            # ask for inputs and try to subtract
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            sub = num1 - num2
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            logger.error("ValueError occurred: invalid numeral.")
        else:
            # If operation passes with no errors, print result
            print(f"The difference is = {sub}.")

    if choice == 3: # multiplication
        try:
            # ask for inputs and try to multiply
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            mult = num1 * num2
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            logger.error("ValueError occurred: invalid numeral.")
        else:
            # If operation passes with no errors, print result
            print(f"The product is = {mult}.")

    if choice == 4: #division
        try:
            # ask for inputs and try to divide
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            div = num1/num2
        except ZeroDivisionError:
            print("Oops! Division by zero is not allowed.")
            logger.error("ZeroDivisionError occurred: division by zero.") #logging ZeroDivisionError to file
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            logger.error("ValueError occurred: invalid numeral.")
        else:
            # If operation passes with no errors, print result
            print(f"The quotient is = {div:.2f}.")# Round result to 2 decimal places

    # Ask again after exception caught/task completion 
    choice = int(input('''Choose an operation:
    1. Addition 
    2. Subtraction 
    3. Multiplication 
    4. Division 
    5. Exit
    Enter your choice (1/2/3/4/5)> ''')) 
# if choice is 5 (exit), exit program
print("Goodbye!")
exit