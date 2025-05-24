"""
Author: Sarina Iqbal
Python Assignment 2 Task 2
"""

number = int(input("Enter a number: "))

# Loop goes from 1 to 10 (included)
for i in range(1,11):
    product = number*i # the product is calculated here
    print(number, "x" , i, "=", product, end=" ") # prints everything in the same line