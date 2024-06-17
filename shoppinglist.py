#2. The Shopping List Maker
#Objective: The aim of this assignment is to create a program that helps users make a shopping list.

#Task 1: Write a function that lets the user add items to a list, make sure you ask the user what they would like to add (reminder: ensure the function has a parameter to receive the list). 
# Task 2: Include a feature to remove items from the list.
#  Task 3: Add a function that prints out the entire list.

def add_item(shopping_list):
    item = input("What would you like to add to your shopping list? ")
    shopping_list.append(item)
    return shopping_list

def remove_item(shopping_list):
    item = input("What would you like to remove from your shopping list? ")
    shopping_list.remove(item)
    return shopping_list

def print_list(shopping_list):
    print(shopping_list)

def shopping_list():
    shopping_list = []
    while True:
        print("1: Add item")
        print("2: Remove item")
        print("3: Print list")
        print("4: Quit")
        choice = input("What would you like to do? ")
        if choice == '1':
            add_item(shopping_list)
        elif choice == '2':
            remove_item(shopping_list)
        elif choice == '3':
            print_list(shopping_list)
        elif choice == '4':
            print("Goodbye")
            break
        else:
            print("Invalid input")



shopping_list()