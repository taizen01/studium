# Beispiel-Liste
arr = [12, 4, 5, 6, 7, 3, 1, 15]
print("Original List:", arr)

stack = [(0, len(arr)-1)]


while stack:
    print('Stack: ' + str(stack)) #Gebe den Aktuellen Stack aus

    start, end = stack.pop()

    left=start
    right=end

    mid = (start + end) // 2
    pivot = arr[mid]

    while left <= right:
        while arr[left] < pivot:
            left+=1
    
        while arr[right] > pivot:
            right-=1

        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left+=1
            right-=1

    ## Füge die   neuen Bereiche hinzu
    if start < right:
        stack.append((start,right))
    
    if left < end:
        stack.append((left,end))

