# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 20:26:18 2022

@author: Daniyar Syrlybayev
"""

from random import randint

def randomized_partition(A, p, r):
    i = randint(p, r)
    A[i], A[r] = A[r], A[i]
    return partition(A, p, r)
    
def partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i+=1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def quick_sort(A, p, r, randomized = True):
    if p < r:
        f = randomized_partition if randomized == True else partition
        q = f(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q+1, r) 
