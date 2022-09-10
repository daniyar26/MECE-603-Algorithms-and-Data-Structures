# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 14:22:07 2022

@author: Daniyar Syrlybayev
"""
import time as tm

def max_subarray(A):
    max_suma = float('-inf')
    for i in range(len(A) - 1):
        for j in range(i+1, len(A)):
            suma = A[j] - A[i]
            if suma >= max_suma:
                max_suma, buy_day, sell_day = suma, i, j
    return buy_day, sell_day, max_suma

start = tm.time()
A1 = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]
A2 = [10, 11, 7, 10, 6]
print(max_subarray(A1))
print(max_subarray(A2))
end = tm.time()
print('Brute Force Execution Time is {:.6f} seconds'.format(end - start))


def rec_max_subarray(A, low, high):
    if low == high:
        return low, high, A[low]
    else:
        mid = (high + low)//2
        left_low, left_high, left_sum = rec_max_subarray(A, low, mid)
        righ_low, right_high, right_sum = rec_max_subarray(A, mid+1, high)
        cross_low, cross_high, cross_sum = max_crossing_subarray(A, low, high, 
                                                                 mid)
        
        if left_sum >= cross_sum and left_sum >= right_sum:
            return left_low, left_high, left_sum
        elif right_sum >= cross_sum and right_sum >= left_sum:
            return righ_low, right_high, right_sum
        else: return cross_low, cross_high, cross_sum

def max_crossing_subarray(A, low, high, mid):
    summa = 0
    max_left = float('-inf')
    for i in range(mid, low-1, -1):
        summa += A[i]
        if summa > max_left: 
            max_left = summa
            start = i
    
    summa = 0
    end = mid + 1
    max_right = float('-inf')
    for i in range(mid+1, high):
        summa += A[i]
        if summa > max_right:
            max_right = summa
            end = i
    return start, end, max_right + max_left
                

start = tm.time()
A1 = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 
      97]
A2 = [10, 11, 7, 10, 6]
B1 = [-abs(A1[i] - A1[i-1]) for i in range(1, len(A1))]
B2 = [-abs(A2[i] - A2[i-1]) for i in range(1, len(A2))]
print(rec_max_subarray(B1, 0, len(B1) -1))
print(rec_max_subarray(B2, 0, len(B2) -1))
end = tm.time()
print('Recursive Execution Time is {:.6f} seconds'.format(end - start))