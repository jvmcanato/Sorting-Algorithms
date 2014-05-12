# -*- coding: utf-8 -*-
import random, time
"""
Shell Sort Algorithm
Worst-case: depends
Animation: http://www.sorting-algorithms.com/animation/50/random-initial-order/shell-sort.gif
@author: João Vitor Mussel Canato
"""

def shellSort(lst):
    gap = 1
    while gap < len(lst):
        gap = 3*gap + 1
    while gap > 1:
        gap /= 3
        for i in range(gap, len(lst)):
            val = lst[i]
            j = i - gap
            while j >= 0 and val < lst[j]:
                lst[j + gap] = lst[j]
                j -= gap
            lst[j + gap] = val
    return lst

lst = range(50)
random.shuffle(lst)

start = time.time()
shellSort(lst)
end = time.time()
#print(lst)
print("Time: " + str(end - start))
