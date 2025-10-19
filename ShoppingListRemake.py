# -*- coding: utf-8 -*-
"""
Created on Sun Oct 19 18:21:44 2025

@author: Isabella
"""

def convert_menu_to_dictionary(menu_file):
    menu_dict = {}
    with open(menu_file, 'r') as file:
        for line in file:
            # Split the line into recipe name and ingredients
            recipe, ingredients = line.strip().split(maxsplit=1)
            # Add the recipe and ingredients to the dictionary
            menu_dict[recipe] = ingredients.split()
    return menu_dict

def display_recipes(menu_dict):
    # Display all available recipes
    print("\nAvailable Recipes:")
    for i, recipe in enumerate(menu_dict.keys(), 1):
        print(f"{i}. {recipe}")
    print()


def choose_recipes(menu_dict):
    # Let the user pick which recipes they want to make
    display_recipes(menu_dict)
    choices = input("Enter the numbers of the recipes you want: ")
    selected_recipes = []
    for num in choices.split(','):
        num = num.strip()
        if num.isdigit() and 1 <= int(num) <= len(menu_dict):
            selected_recipes.append(list(menu_dict.keys())[int(num) - 1])
    return selected_recipes

def make_grocery_list(menu_dict):
    grocery_list = set()
    for ingredients in menu_dict.values():
        grocery_list.update(ingredients)
    return grocery_list

def display_grocery_list(grocery_list):
    print("Grocery List:")
    for item in sorted(grocery_list):
        print(item)

def save_grocery_list_to_file(grocery_list, file_name):
    with open(file_name, 'w') as file:
        for item in sorted(grocery_list):
            file.write(item + '\n')

# Convert menu.txt to dictionary
menu_file = "menu.txt"
menu_dict = convert_menu_to_dictionary(menu_file)

# Create grocery list
grocery_list = make_grocery_list(menu_dict)

# Display grocery list
display_grocery_list(grocery_list)

# Save grocery list to external file
save_grocery_list_to_file(grocery_list, "grocerylist.txt")
def convert_menu_to_dictionary(menu_file):
    menu_dict = {}
    with open(menu_file, 'r') as file:
        for line in file:
            # Split the line into recipe name and ingredients
            recipe, ingredients = line.strip().split(maxsplit=1)
            # Add the recipe and ingredients to the dictionary
            menu_dict[recipe] = ingredients.split()
    return menu_dict

def make_grocery_list(menu_dict):
    grocery_list = set()
    for ingredients in menu_dict.values():
        grocery_list.update(ingredients)
    return grocery_list

def display_grocery_list(grocery_list):
    print("Grocery List:")
    for item in sorted(grocery_list):
        print(item)

def save_grocery_list_to_file(grocery_list, file_name):
    with open(file_name, 'w') as file:
        for item in sorted(grocery_list):
            file.write(item + '\n')

# Convert menu.txt to dictionary
menu_file = "menu.txt"
menu_dict = convert_menu_to_dictionary(menu_file)

# Create grocery list
grocery_list = make_grocery_list(menu_dict)

# Display grocery list
display_grocery_list(grocery_list)

# Save grocery list to external file
save_grocery_list_to_file(grocery_list, "grocerylist.txt")
