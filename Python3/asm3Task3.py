"""
Author: Sarina Iqbal
Python Assignment 3 Task 3
"""

word = input("Enter a word: ")

word_rev = word[::-1] # Reverse string using slicing with index(0:end:step = -1)

if word.lower()==word_rev.lower(): # compare the lowercase forms so method is not case-sensitive
    print("Yes, '" + word + "' is a palindrome!")
else:
    print("The word is not a palindrome.")