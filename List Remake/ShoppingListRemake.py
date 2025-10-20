# -*- coding: utf-8 -*-
"""
Created on Sun Oct 19 18:21:44 2025

@author: Isabella
"""


# Grocery list program with menu file and ingredient amounts
def load_menu(filename):
    menu = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                if ':' in line:
                    recipe, ingredients = line.strip().split(':', 1)
                    ingredient_list = [i.strip() for i in ingredients.split(',')]
                    menu[recipe.strip()] = ingredient_list
    except FileNotFoundError:
        print(f"Warning: {filename} not found. Using embedded menu instead.")
    return menu

# Embedded menu as a dictionary
embedded_menu = {
    "Pasta": ["200g noodles", "150ml tomato sauce", "50g cheese", "5g Basil", "100g meatballs"],
    "Salad": ["100g lettuce", "50g tomato", "50g cucumber", "30ml dressing"],
    "Tacos": ["3 tortillas", "200g beef", "50g cheese", "50g salsa", "30g lettuce"],
    "Sandwich": ["2 slices bread", "50g ham", "50g cheese", "20g lettuce", "30g tomato"]
}

# Show the user all available recipes
def show_recipes(menu):
    print("\nAvailable Recipes:")
    for i, recipe in enumerate(menu.keys(), start=1):
        print(f"{i}. {recipe}")

# Let the user pick one or more recipes they want to make
def choose_recipes(menu):
    show_recipes(menu)
    choices = input("\nEnter the numbers of the corresponding recipes you want to make: ")
    chosen = []
    for choice in choices.split(','):
        choice = choice.strip()
        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(menu):
                recipe = list(menu.keys())[index]
                chosen.append(recipe)
    return chosen

# Ask if user has each ingredient; collect missing ones (with amounts)
def check_ingredients(menu, chosen_recipes):
    grocery_list = []
    for recipe in chosen_recipes:
        print(f"\nChecking ingredients for {recipe}:")
        for ingredient in menu[recipe]:
            while True:
                have_it = input(f"Do you have '{ingredient}'? (y/n): ").strip().lower()
                if have_it in ['y', 'n']:
                    break
                else:
                    print("Please enter 'y' or 'n'.")
            
            if have_it == 'y':
                # Ask if they have enough
                while True:
                    enough = input(f"Do you have enough of '{ingredient}'? (y/n): ").strip().lower()
                    if enough in ['y', 'n']:
                        break
                    else:
                        print("Please enter 'y' or 'n'.")
                if enough == 'n':
                    grocery_list.append(ingredient)
            else:
                grocery_list.append(ingredient)
    return grocery_list

# Remove duplicates from grocery list
def remove_duplicates(grocery_list):
    return list(dict.fromkeys(grocery_list)) 

# Show the grocery list to the user
def show_grocery_list(grocery_list):
    print("\nGrocery List:")
    if grocery_list:
        for item in grocery_list:
            print(f"- {item}")
    else:
        print("You already have everything you need!")

# Save the grocery list to a file
def save_grocery_list(filename, grocery_list):
    with open(filename, 'w') as file:
        if grocery_list:
            for item in grocery_list:
                file.write(f"{item}\n")
        else:
            file.write("You already have everything you need!\n")
    print(f"\nGrocery list saved to '{filename}'.")

# Main program flow
def main():
    menu_file = "menu.txt"
    menu_dict = load_menu(menu_file)

    if not menu_dict:
        menu_dict = embedded_menu

    chosen_recipes = choose_recipes(menu_dict)
    if not chosen_recipes:
        print("No recipes selected.")
        return

    grocery_list = check_ingredients(menu_dict, chosen_recipes)
    grocery_list = remove_duplicates(grocery_list)

    show_grocery_list(grocery_list)
    save_grocery_list("grocerylist.txt", grocery_list)

if __name__ == "__main__":
    main()
