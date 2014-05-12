# -*- coding: utf-8 -*-
import random, time
"""
Selection Sort Algorithm
Worst-case: O(n²)
Animation: http://www.sorting-algorithms.com/animation/50/random-initial-order/selection-sort.gif
@author: João Vitor Mussel Canato
"""

def selectionSort(lst):
    for i in range(len(lst) - 1):
        min = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min]:
                min = j
        if min != i:
            val = lst[i]
            lst[i] = lst[min]
            lst[min] = val
    return lst
    
lst = range(50)
random.shuffle(lst)

start = time.time()
selectionSort(lst)
end = time.time()
#print(lst)
print("Time: " + str(end - start))
