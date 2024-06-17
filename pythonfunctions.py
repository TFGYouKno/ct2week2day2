#1. The Calculator App
#Objective: The aim of this assignment is to build a basic calculator that can perform addition, subtraction, multiplication, and division.

#Task 1: Create functions for each arithmetic operation, with parameters for two numbers to be used in the operation. 
#Task 2: Implement user input to receive numbers and an operation choice, their response for operation should call the associated function

def add(num1, num2):
    return num1 + num2

def subtract():
    return num1 - num2

def multiply():
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def calculator():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")
    if operation == '+':
        print(add(num1, num2))
    elif operation == '-':
        print(subtract(num1, num2))
    elif operation == '*':
        print(multiply(num1, num2))
    elif operation == '/':
        print(divide(num1, num2))
    else:
        print("Invalid input")

calculator()

