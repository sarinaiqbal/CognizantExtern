"""
Author: Sarina Iqbal
Python Assignment 2 Task 3
"""

number = int(input("Enter a number: "))

copy = number #create a copy of the number so original is unchanged

# Loop goes from 1 to number-1 (included)
for i in range(1, number):
    copy = copy * i # calculate factorial
print("The factorial of", number, "is", copy)