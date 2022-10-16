# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 15:28:59 2022

@author: Daniyar Syrlybayev
"""

class Stack:
    def __init__(self, n, *L):
        if len(L) >= n:
            raise('Size of the input is less than stack size')
        else:
            self.A = []
            self.top = -1
            self.size = n
            for i in L:
                self.A.append(i)
                self.top += 1
            
            for i in range(len(self.A) + 1, n+1):
                self.A.append(None)
        return None
    
    def __str__(self):
        return str(self.A)
    
    def stack_empty(self):
        if self.top == -1:
            return True
        else: return False
    
    def push(self, k):
        if self.top == self.size-1:
            raise('Stack overflow')
        else:
            self.top += 1
            self.A[self.top] = k
    
    def pop(self):
        if self.top == -1:
            raise('Stack underflow')
        else:
            x = self.A[self.top]
            self.A[self.top] = None
            self.top -= 1
            return x
