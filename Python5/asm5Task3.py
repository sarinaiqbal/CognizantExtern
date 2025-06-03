'''
Author: Sarina Iqbal
Assignment: About Parameters of Functions
Task 3
'''

def make_sandwich(*args):
    print("Making a sandwich with the following ingredients:")
    for item in args:
        print(" - " + item) # Prints items as a list

make_sandwich("jelly", "bun", "ham") # Calling function with 3 arguments