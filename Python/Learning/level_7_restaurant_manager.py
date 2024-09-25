import os

#### Dictionary

def display_menu(n):
    for key, value in n.items():
        print(f'Dish: {key} - Category: {value[0]} | Price: ${value[1]}')
        

def dish_type_count(menu):
    types = {"Appetizer":0,"Dessert":0,"Drink":0,"Main":0}
    for i in menu.values():
        if i[0] in types.keys():
            types[i[0]] += 1
    return types

def dish_type_count_v2(menu):
    types = {}
    for i in menu.values():
        if i[0] in types:
            types[i[0]] += 1
        else:
            types[i[0]] = 1
    return types

def update_price(menu, name, price):
    lst = menu.get(name)
    menu[name] = (lst[0], price)
    return "\nPrice change executed\n"

def update_price_v2(menu, name, price):
    if name in menu:
        menu[name] = (menu[name][1],price)   #Tupel erlauben keine item assigments, hier war die Lösung ein neuen Tupel als Wert einzufügen!
    else:
        return "Item was not found."
    return "Price was changed."

######################################

os.system("cls")

menu = {
    "Burger": ("Main", 10.5),
    "Soup": ("Appetizer", 5.0),
    "Ice Cream": ("Dessert", 3.5),
    "Salad": ("Appetizer",2.5)
}

menu["Steak"] = ("Main", 14.5)
menu["Soda"] = ("Drink", 5.0)
wert = menu.pop("Salad")


print(update_price_v2(menu, "Burger", 15))
print(update_price_v2(menu, "Steak", 400))

display_menu(menu)

print(dish_type_count_v2(menu))