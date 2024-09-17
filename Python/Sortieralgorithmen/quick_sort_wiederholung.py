### quick_sort wiederholung
arr = [5,2,12,7,1,8,9,11]
print("Originaler Stack: " + str(arr))

### len(arr)-1 da sonst der Bereich nicht mehr stimmt. Wegen der len() Funktion zählt die Null nicht mit.
stack = [(0,len(arr)-1)]

while stack: # Solange der Stack in der iterativen qick_sort Sortierung noch nicht leer führe die sortierung durch.
    start,end = stack.pop()         # Übernehme den Bereich von Anfang bis Ende des jeweiligen Stack Tupels

    left=start # Zähler für linken Bereich des mittleren Pivots
    right=end # Zähler für rechten Bereich des mittleren Pivots

    pivot = arr[(len(arr)//2)]

    # Schleife die die eigentliche Sortierung bis zum Pivot durchführt
    while left < right:
        while arr[left] < pivot:
            left+=1
        while arr[right] > pivot:
            right-=1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left+=1
            right-=1

    # Prüfen welcher Bereich bereits sortiert ist und ggbfs. diesen dem Stack hinzufügen zur erneuten Sortierung
    if right < left:
        stack.append((start,right))
    
    if right < end:
        stack.append((left,end))

print("Sortierter Stack: " + str(arr))


