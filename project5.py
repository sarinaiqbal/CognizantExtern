'''
Author: Sarina Iqbal
Python Project: About Menu
Description: This program presents a menu of choices to carry out three different
operations: calculating a Factorial, finding the nth Fibonacci number, and 
drawing a recursive fractal tree. The program ends after the completion of
a single task without errors, and needs to be re-run to use the other tasks.
'''

import turtle

# Presenting menu of choices in the beginning
print('''Welcome to the Recursive Artistry Program!
      
    Menu of choices:
    Enter 1 to calculate the factorial of a number.
    Enter 2 to find the nth Fibonacci number.
    Enter 3 to draw a recursive fractal tree.
    Enter 4 to exit the program.''')

choice = int(input('''Enter the number for your selected option: '''))

# Function to calculate the factorial of a number
def factorial(number):
    if number == 0 or number == 1: # base case, 0! = 1! = 1
        return 1
    else: # recursive case
        return number * factorial(number-1)

# Function to find the nth Fibonacci number
def fibonacci(number):
    # base cases
    if number == 0: 
        return 0
    if number == 1 or number == 2:
        return 1
    else: # recursive case
        return fibonacci(number-1) + fibonacci(number-2) 
    
# Recursive function that draws the fractral tree
def draws(branch, tree):
    if branch<=10: #  # Base case, if branch is too short, skip
        return
    else:
        tree.forward(branch) # Create main branch
        tree.left(15) # Move 15 degrees left and draw sub branch
        # Recursive call on shorter branch
        draws(branch-15, tree) 
        tree.right(30) # Move 30 degrees right and draw sub branch
        draws(branch-15, tree) 
        # Recursive call on shorter branch
        tree.left(15) # Move 15 degrees left and draw sub branch
        tree.backward(branch) # Move back to previous branch

# Function that displays the fractral tree on a screen
def fractal():
    screen = turtle.Screen() # Screen to draw
    tree = turtle.Turtle() # Create a Turtle object called tree
    # Positioning drawing cursor, starting point of tree
    # and ensuring it is vertically upright
    tree.left(90) 
    tree.up() 
    tree.backward(100)
    tree.down()
    tree.speed(10) # Speed of drawing tree
    draws(80,tree) # Draw tree from a position
    screen.mainloop() # GUI window stays open till exited


if choice == 1: 
    while True: # Loop to ask for input again incase of error
        try:
            user_number = int(input("Enter a number to find its factorial: "))
            # Raise Error for negative inputs
            if user_number<0:
                raise ValueError("No negative numbers.")
            factorial_res = factorial(user_number)
        except ValueError: # Error message for non-numeral and negative inputs
            print("Invalid input! Please enter a valid positive integer.")
        # Print result with a final message if task completes without
        # errors and break out of loop
        else: 
            print(f"The factorial of {user_number} is {factorial_res}.")
            print()
            print("Thank you! Please run the program again to explore the other options.")
            break
            

elif choice == 2:
    while True: # Loop to ask for input again incase of error
        try:
            user_pos = int(input("Enter the position of the Fibonacci number: "))
            # Raise Error for negative inputs
            if user_pos<0:
                raise ValueError("No negative numbers.")
            fibonacci_res = fibonacci(user_pos)
        except ValueError: # Error message for non-numeral and negative inputs
            print("Invalid input! Please enter a valid positive integer.")
        # Print result with a final message if task completes without
        # errors and break out of loop
        else: 
            print(f"The Fibonacci number at position {user_pos} is {fibonacci_res}.")
            print()
            print("Thank you! Please run the program again to explore the other options.")
            break            

elif choice == 3:
    print("Please view the GUI window.")
    fractal()
    # Print a final message
    print("Thank you! Please run the program again to explore the other options.")

elif choice==4:
    # If choice==4, exit the program
    print("Goodbye!")
    exit
