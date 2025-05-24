"""
Author: Sarina Iqbal
Python Assignment 2 Task 1
"""

number = int(input("Enter the starting number: "))

while number > 0:
    print(number, end=" ")
    number-=1 # Decrement number to print backwards
print("Blast off!")