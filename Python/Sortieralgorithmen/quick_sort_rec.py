# Beispiel-Array
import random

arr = [12, 4, 5, 6, 7, 3, 1, 15, 9, 2, 1, 4]
print("Unsortiertes Array:", arr)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        piv = arr[len(arr)-1]
        left = [x for x in arr[:-1] if x < piv] #list comprehension: to create a newlist based on a if statement
        right = [x for x in arr[:-1] if x >= piv]
        print(piv)
        print(left)
        print(right)
        return quick_sort(left) + [piv] + quick_sort(right)

print(quick_sort(arr)) 
