'''
Author: Sarina Iqbal
Assignment: About Parameters of Functions
Task 1
'''

def greet_user(name):
    print("Hello there " + name + "!")

def add_numbers(num1, num2):
    return num1 + num2

greet_user("Alice") #Calling first function with name Alice
print(f"The sum of 5 and 10 is {add_numbers(5, 10)}.") # Calling second function with numbers 5 and 10