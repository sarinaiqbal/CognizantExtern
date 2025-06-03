'''
Author: Sarina Iqbal
Assignment: About Parameters of Functions
Task 4
'''
# Function to calculate factorial
def factorial(number):
    # base case
    if number == 1:
        return 1
    # recursive case
    else:
        return number * factorial(number-1)

# Function to find nth number in Fibonacci sequence
def fibonacci(number):
    # base cases
    if number == 0:
        return 0
    if number == 1 or number == 2:
        return 1
    # recursive case
    else:
        return fibonacci(number-1) + fibonacci(number-2)
    

print(f"The factorial of 4 is {factorial(4)}.") # Finding 4!
print(f"The 5th Fibonacci number is {fibonacci(5)}.") # Finding 5th number in Fibonacci sequence