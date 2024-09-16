### Abfrage wie groß der Baum werden soll
size = int(input("Bitte gebe die größe des Baumes an: "))

## Baumerstellung mittels Schleife
i = 0
k = size

while i <= size:
    j = "*"
    baum = 2*(i * j)
    space = " "
    baumstar = 'x'
    baumspace = k * space
    if i >= 1:
        print(baumspace + baum)
    else:
        print(baumspace + baumstar)
    i+=1
    k-=1



