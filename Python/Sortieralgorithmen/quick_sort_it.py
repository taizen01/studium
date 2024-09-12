# Beispiel-Liste
arr = [12, 4, 5, 6, 7, 3, 1, 15]
print("Original Array:", arr)

# Stack, um die Bereiche zu speichern, die noch sortiert werden müssen
stack = [(0, len(arr) - 1)]
print("Initial Stack:", stack)

# Verarbeite den Stack
while stack:
    start, end = stack.pop()  # Hole den Bereich vom Stack
    print(f"\nPopped from stack: start={start}, end={end}")

    if start >= end:
        continue  # Wenn der Bereich nur 0 oder 1 Element hat, überspringen
    print("Processing range:", arr[start:end+1])

    # Wähle das Pivot (Median)
    mid = (start + end) // 2
    pivot = arr[mid]
    print(f"Pivot: {pivot} at index {mid}")

    # Initialisiere linke und rechte Zeiger
    left = start
    right = end

    # Partitionierung
    while left <= right:
        # Bewege den linken Zeiger nach rechts, bis ein Element größer oder gleich dem Pivot gefunden wird
        while arr[left] < pivot:
            left += 1
            print(left)
        # Bewege den rechten Zeiger nach links, bis ein Element kleiner oder gleich dem Pivot gefunden wird
        while arr[right] > pivot:
            right -= 1
            print(right)

        # Tausche die Elemente, wenn sich die Zeiger nicht überschneiden
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            print(f"Swapped elements at indices {left} and {right}: {arr}")
            left += 1
            right -= 1

    # Zeiger nach Partitionierung
    print("Array after partitioning:", arr)

    # Füge die neuen Bereiche in den Stack ein
    if start < right:
        stack.append((start, right))  # Bereich links vom Pivot
        print(f"Added to stack: ({start}, {right})")
    if left < end:
        stack.append((left, end))     # Bereich rechts vom Pivot
        print(f"Added to stack: ({left}, {end})")

    print("Current Stack:", stack)

print("\nSorted Array:", arr)
