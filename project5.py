'''
Author: Sarina Iqbal
'''

import turtle

print("Menu of choices:")
print("Enter 1 to calculate the factorial of a number. ")
print("Enter 2 to find the nth Fibonacci number.")
print("Enter 3 to draw a recursive fractal pattern")
print("Enter 4 to exit the program.")

choice = int(input("Enter the number for your selected option: "))

def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number-1)

def fibonacci(number):
    if number == 0:
        return 0
    if number == 1 or number == 2:
        return 1
    else:
        return fibonacci(number-1) + fibonacci(number-2) 
    
def draws(branch, t):
    if branch > 10:
        t.forward(branch)
        t.right(20)
        draws(branch-15, t)
        t.left(40)
        draws(branch-15, t)
        t.right(20)
        t.backward(branch)


def fractal():
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    t.speed(0)
    draws(75,t)
    screen.exitonclick()
    

if choice == 1:
    user_number = int(input("Enter a number to find its factorial: "))
    print(factorial(user_number))
elif choice == 2:
    user_pos = int(input("Enter the position of the Fibonacci number: "))
    print(fibonacci(user_pos))
elif choice == 3:
    fractal()
else:
    exit
