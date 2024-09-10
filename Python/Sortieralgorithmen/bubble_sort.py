import random
import time

### Deklariere Variable
lst = []

eingabe = input("Bitte gebe die Anzahl an zu generierenden Zahlen ein: ")

for i in range(int(eingabe)):
    lst.append(random.randint(0,100))
    i+=1

print("Unsortiert: " + str(lst))

length = len(lst)

start = time.time()
for i in range(length):
    for j in range(length-1-i):
        if lst[j]>lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]  #Vertausche wenn 1. Element größer als 2.Element
        j+=1
    i+=1
end = time.time()
result = end - start

print("Sortiert: " + str(lst))
print("Dauer der Berechnung: " + str(result) + " sek")

