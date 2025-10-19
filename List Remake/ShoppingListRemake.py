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

def check_ingredients(menu_dict, selected_recipes):
    # For each selected recipe, ask if the user has the ingredients
    grocery_items = set()
    for recipe in selected_recipes:
        print(f"\nChecking ingredients for '{recipe}':")
        for ingredient in menu_dict[recipe]:
            have_it = input(f"Do you have '{ingredient}'? (cay/n): ").lower()
            if have_it != 'y':
                grocery_items.add(ingredient)
    return sorted(grocery_items)

def display_grocery_list(grocery_list):
    # Display the final grocery list without duplicates
    print("\nGrocery List:")
    if grocery_list:
        for item in grocery_list:
            print(f"- {item}")
    else:
        print("You already have everything you need!")


def save_grocery_list_to_file(grocery_list, file_name):
    # Save the grocery list to an external file
    with open(file_name, 'w') as file:
        for item in grocery_list:
            file.write(item + '\n')
    print(f"\nGrocery list saved to '{file_name}'.")

def main():
    # Convert menu.txt to dictionary
    menu_file = "menu.txt"
    menu_dict = convert_menu_to_dictionary(menu_file)

    # Let the user pick recipes
    selected_recipes = choose_recipes(menu_dict)

    # Check ingredients and create grocery list
    grocery_list = check_ingredients(menu_dict, selected_recipes)

    # Display grocery list
    display_grocery_list(grocery_list)

    # Save grocery list to external file
    save_grocery_list_to_file(grocery_list, "grocerylist.txt")


if __name__ == "__main__":
    main()
