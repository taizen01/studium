frage1 = input("Wie viele 1. Klasse Tickets möchten sie kaufen?\n")
frage2 = input("Wie viele 2. Klasse Tickets möchten sie kaufen?\n")
frage3 = input("Wie viele 3. Klasse Tickets möchten sie kaufen?\n")

first_class = 870
second_class = 100.42
third_class = 7

gesamtpreis = int(frage1)*first_class+int(frage2)*second_class+int(frage3)*third_class

print(f"Der Gesamtpreis für die Tickets liegt bei {gesamtpreis:.2f} pounds.")
