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
