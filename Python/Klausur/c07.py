def pig_latin(n):
    n = n.lower()
    if n.startswith(("A", "E", "I", "O", "U")):
            return f"{n[1::]}way"
    else:
            return f"{n[1::]}{n[0]}ay"


x = input("Bitte gebe eine Wort ein: ")

print(pig_latin(x))