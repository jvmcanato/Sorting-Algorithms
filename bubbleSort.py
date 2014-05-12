# -*- coding: utf-8 -*-
import random, time
"""
Bubble Sort Algorithm
Worst-case: O(n²)
Animation: http://www.sorting-algorithms.com/animation/50/random-initial-order/bubble-sort.gif
@author: João Vitor Mussel Canato
"""

def bubbleSort(lst):
    for i in range(len(lst) - 1):
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                val = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = val
    return lst
    
lst = range(50)
random.shuffle(lst)

start = time.time()
bubbleSort(lst)
end = time.time()
#print(lst)
print("Time: " + str(end - start))
