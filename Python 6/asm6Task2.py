'''
Author: Sarina Iqbal
Python Assignment 6 Task 2
'''

''' Handling IndexError by accessing an invalid list index.'''
numbers = ["one", "two", "three"]
# List 'numbers' has three elements with index 0,1,2 respectively. 

try:
    print(numbers[4]) # Trying to access a nonexistent index 4 or 5th element gives an IndexError.
except IndexError as e:
    print("IndexError occured. List index out of range.")


'''Handling KeyError by trying to access a non-existent key in a dictionary.'''
dicti = {"book":"store", "race":"car"} # Dictionary with keys 'book' and 'race'

# A function to raise error incase of nonexistent key
def keys_check(word):
    if word not in dicti:
        # Raise KeyError if key not in dictionary
        raise KeyError(f"KeyError occurred! Key not found in the dictionary.")
    val = dicti[word] # find value if key in dictionary

try:
    keys_check("wood") # trying to access a non-existent key
except KeyError as e:
    print(f"{e}") # Print error message in case of error

'''Handling TypeError by adding a string and an integer.'''
str = "12345"
integer = 123
try:
    # try adding the string and integer
    # this gives an error because string and ints are incompatible types and cannot be added
    print(str + integer) 
except TypeError as e:
    print("TypeError occurred! Unsupported operand types.") # Print error message in case of error