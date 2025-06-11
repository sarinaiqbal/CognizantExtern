"""
Author: Sarina Iqbal
Python Project 3: Password Strength Checker
A program to check password strength. Takes input for a password and determines 
its strength based on given requirements. A score of 10 indicates the strongest 
and 0 is the weakest password. 
"""

password = input("Enter a password: ")

upcount = 0 # keep count of upper case characters
lowcount = 0 # keep count of lower case characters
digcount = 0 # keep count of digits
special = "!?<>@#$%^&*-+=_" # possible special chars
spcount = 0 # keep count of special characters
score = 10 # initial score set to 10 (strongest)

# Loop goes from 0 to len(password)-1
for i in range(len(password)):
    if password[i].isupper():
        upcount+=1 # increment if upper case char found 
    if password[i].islower():
        lowcount += 1 # increment if lower case char found 
    if password[i].isdigit():
        digcount += 1 # increment if digit char found 
    if password[i] in special:
        spcount += 1 # increment if special char found 

if upcount >=1 and lowcount >= 1 and digcount >= 1 and spcount >= 1 and len(password)>=8:
    score = 10 # All requirements met, full score
    print(f"Your password is strong!")
else:
    print("Your password needs: ")
    if upcount < 1: # There is no uppercase
        score -= 2 
        print(" - At least one uppercase letter")
    if lowcount < 1: # There is no lowercase
        score -= 2
        print(" - At least one lowercase letter")
    if digcount < 1: # There are no digits
        score -= 2
        print(" - At least one digit")
    if spcount < 1: # There are no special chars
        score -= 2
        print(" - At least one special character")
    if len(password) < 8: # Password has less than 8 chars
        score = 0 # if length < 8, score is 0
        print(" - At least 8 characters")
    
# Printing final password strength score
print(f"Your password strength score is: {score} (10: strongest; 0: weakest)")

# Example runs:
# The password: python gets a score of 0 as it has less than 8 characters.
# The password: Python13 gets a score of 8 as it does not have special characters.
# The password: ra!nyday gets a score of 6 as it does not have digits and upper case characters.
