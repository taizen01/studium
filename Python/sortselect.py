#!/bin/usr/env python
#Sortselect Übung
import random

#Generate radom numbers to list
i = 0
unsorted = []
while i < 10:
    unsorted.append(random.randint(0, 100))
    i = i + 1

print(unsorted)

counter = 0
while counter < len(unsorted):
    index = counter
    minPos = counter
    replace = counter

    while index < len(unsorted):
        if unsorted[minPos] > unsorted[index]:
            minPos = index
        else:
            index = index + 1

    switch = unsorted[minPos]
    unsorted[minPos] = unsorted[replace]  
    unsorted[replace] = switch
    counter = counter + 1
    
print(unsorted)