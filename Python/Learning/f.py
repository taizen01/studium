menu = {
    "Burger": ("Main", 10.5),
    "Soup": ("Appetizer", 5.0),
    "Ice Cream": ("Dessert", 3.5),
    "Salad": ("Appetizer",2.5)
}

types = {"Appetizer":0,"Dessert":0,"Drink":0,"Main":0}
for i in menu.values():
    tup = i
    if tup[0] in types.keys():
        types[tup[0]] += 1
        print(types)