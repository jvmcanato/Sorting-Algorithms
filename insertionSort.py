# -*- coding: utf-8 -*-
import random, time
"""
Insertion Sort Algorithm
Worst-case: O(n²)
Animation: http://www.sorting-algorithms.com/animation/50/random-initial-order/insertion-sort.gif
@author: João Vitor Mussel Canato
"""

def insertionSort(lst):
    for i in range(1, len(lst)):
        val = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > val:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = val
    return lst

lst = range(50)
random.shuffle(lst)

start = time.time()
insertionSort(lst)
end = time.time()
#print(lst)
print("Time: " + str(end - start))
