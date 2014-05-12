# -*- coding: utf-8 -*-
import random, time
"""
Merge Sort Algorithm
Worst-case: O(nlogn)
Animation: http://www.sorting-algorithms.com/animation/50/random-initial-order/merge-sort.gif
@author: João Vitor Mussel Canato
"""

def merge(lst1, lst2):
    res = []
    i, j = 0, 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] <= lst2[j]:
            res.append(lst1[i])
            i += 1
        else:
            res.append(lst2[j])
            j += 1
    while i < len(lst1):
        res.append(lst1[i])
        i += 1
    while j < len(lst2):
        res.append(lst2[j])
        j += 1
    return res

def mergeSort(lst):
    if len(lst) <= 1:
        return lst
    else:
        mid = len(lst) / 2
        return merge(mergeSort(lst[:mid]), mergeSort(lst[mid:]))

lst = range(50)
random.shuffle(lst)

start = time.time()
lst = mergeSort(lst)
end = time.time()
#print(lst)
print("Time: " + str(end - start))
