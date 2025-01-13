arr = [3,5,8,1,4,9,6,7,2,10]


def mergesort(arr):
    if len(arr) <= 1:  # Base case: an array of 1 or 0 elements is already sorted
        return arr

    # Find the middle index
    middle = len(arr) // 2

    # Split the array into left and right halves
    left = [arr[i] for i in range(middle)]
    right = [arr[i] for i in range(middle, len(arr))]

    # Recursively sort both halves
    left_sorted = mergesort(left)
    right_sorted = mergesort(right)

    # Merge the sorted halves
    return merge(left_sorted, right_sorted)

def merge(left, right):
    result = []
    i = 0 #Zeiger für linke Hälfte
    j = 0 #Zeiger für rechte Hälfte

    # Merge two sorted arrays
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append any remaining elements in `left` or `right`
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

print(mergesort(arr))