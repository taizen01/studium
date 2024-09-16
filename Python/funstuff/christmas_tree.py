### Abfrage wie groß der Baum werden soll
size = int(input("Bitte gebe die größe des Baumes an: "))
stern = input("Was möchtest du als Stern dekorieren? ")

## Variable für das richtige Spacing am Anfang der ersten Ausgabe
k = size

## Baumerstellung mittels Schleife
for i in range(0, size):
    j = "."
    baum = 2*(i * j)+j
    space = " "
    baumstar = stern
    baumspace = (k * space)
    if i >= 1:         #Um die erste Ausgabe zu überspringen und stattdessen den Stern mit dem richtigen Spacing auszugeben. 10 mal leerzeichen mit Sternchen.
        print(baumspace + baum)
    else:
        print(baumspace + baumstar)
    k-=1



