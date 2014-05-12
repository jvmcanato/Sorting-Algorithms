# -*- coding: utf-8 -*-
import random, time
"""
Quick Sort Algorithm
Worst-case: O(n²)
Animation: http://www.sorting-algorithms.com/animation/50/random-initial-order/quick-sort.gif
@author: João Vitor Mussel Canato
"""

def quickSort(lst):
    if len(lst) <= 1:
        return lst
    less, equal, greater = [], [], []
    pivot = lst[0]
    for i in lst:
        if i < pivot:
            less.append(i)
        elif i == pivot:
            equal.append(i)
        else:
            greater.append(i)
    return quickSort(less) + equal + quickSort(greater)

lst = range(50)
random.shuffle(lst)

start = time.time()
lst = quickSort(lst)
end = time.time()
#print(lst)
print("Time: " + str(end - start))
