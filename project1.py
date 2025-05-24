"""
Author: Sarina Iqbal
Python Project 1: Eligible Elector
"""

# Taking integer input for age
age = int(input("How old are you? "))
wait = 0 # an integer placeholder to calculate age difference later

# If age is greater than or equal to 18 print a warm message
if age >=18:
    print("Congratulations! You are eligible to participate!")

else:
    # If age is lesse than 18 print a message with number of years left to turn 18
    wait = 18-age
    print("Sorry, you are not eligible yet. But you only have", wait , "more years to go!")