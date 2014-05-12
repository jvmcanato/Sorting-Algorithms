# -*- coding: utf-8 -*-
import random, time
"""
Heap Sort Algorithm
Worst-case: O(nlogn)
Animation: http://www.sorting-algorithms.com/animation/50/random-initial-order/heap-sort.gif
@author: João Vitor Mussel Canato
"""

def siftdown(lst, start, end):
    root = start
    while True:
        child = 2*root + 1
        if child > end:
            break
        if child + 1 <= end and lst[child] < lst[child + 1]:
            child += 1
        if lst[root] < lst[child]:
            val = lst[root]
            lst[root] = lst[child]
            lst[child] = val
            root = child
        else:
            break

def heapSort(lst):
    for start in range((len(lst) - 2) / 2, -1, -1):
        siftdown(lst, start, len(lst) - 1)
    for end in range(len(lst) - 1, 0, -1):
        val = lst[end]
        lst[end] = lst[0]
        lst[0] = val
        siftdown(lst, 0, end - 1)
    return lst

lst = range(50)
random.shuffle(lst)

start = time.time()
heapSort(lst)
end = time.time()
#print(lst)
print("Time: " + str(end - start))
