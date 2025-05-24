"""
Author: Sarina Iqbal
Python Assignment 3 Task 2
"""

str_val = " hello, python world! "

str_strip = str_val.strip() # Remove extra spaces
str_cap = str_strip.capitalize() # Capitalize the first letter
str_rep = str_val.replace("world", "universe") # Replace "world" with "universe"
str_up = str_val.upper() # Convert the string to uppercase

print("With no extra spaces: " + str_strip)
print("First letter capitalized: " + str_cap)
print("Word replaced: " + str_rep)
print("Uppercase: " + str_up)
