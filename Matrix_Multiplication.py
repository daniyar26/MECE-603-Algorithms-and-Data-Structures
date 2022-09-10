# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 17:16:57 2022

@author: Daniyar Syrlybayev
"""

from numpy import zeros, array

def matrix_multiply(M1, M2):
    assert(len(M1) == len(M2))
    n = len(M1)
    C = zeros((n, n), dtype = int)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i, j] += M1[i][k] * M2[k][j]
    return C

M1 = array([[1, 2], [3, 4]])
M2 = array([[5, 6], [7, 8]])

print(matrix_multiply(M1, M2))

def rec_matrix_multiply(M1, M2):
    assert(len(M1) == len(M2))
    C = zeros((len(M1), len(M1)))
    if len(M1) == 1:
        C[0, 0] = M1[0][0] * M2[0][0]
        return C
    else:
        n = len(M1)
        mid = n//2

        C[:mid, :mid] = (rec_matrix_multiply(M1[:mid, :mid], M2[:mid, :mid]) +
               rec_matrix_multiply(M1[:mid, mid:], M2[mid:, :mid]))
        
        C[:mid, mid:] = (rec_matrix_multiply(M1[:mid, :mid], M2[:mid, mid:]) +
               rec_matrix_multiply(M1[:mid, mid:], M2[mid:, mid:]))
        
        C[mid:, :mid]  = (rec_matrix_multiply(M1[mid:, :mid], M2[:mid, :mid]) +
               rec_matrix_multiply(M1[:mid, mid:], M2[mid:, :mid]))
        
        C[mid:, mid:] = (rec_matrix_multiply(M1[mid:, :mid], M2[:mid, mid:]) +
               rec_matrix_multiply(M1[mid:, mid:], M2[mid:, mid:]))
        return C

print(rec_matrix_multiply(M1, M2))


def rec_matrix_strassen(M1, M2):
    rec_matrix_strassen.counter = 0
    assert(len(M1) == len(M2))
    C = zeros((len(M1), len(M2)))
    if len(M1) == 1:
        C[0, 0] = M1[0][0] * M2[0][0]
        return C
    else:
        mid = len(M1)//2
        A11, A12, A21, A22 = (M1[:mid, :mid], M1[:mid, mid:], M1[mid:, :mid],
                      M1[mid:, mid:])
        
        B11, B12, B21, B22 = (M2[:mid, :mid], M2[:mid, mid:], M2[mid:, :mid],
                      M2[mid:, mid:])
    
        S1, S2, S3, S4, S5, S6, S7, S8, S9, S10 = ((B12 - B22), (A11 + A12), 
                                                   (A21 + A22), (B21 - B11),
                                                   (A11 + A22), (B11 + B22),
                                                   (A12 - A22), (B21 + B22),
                                                   (A11 - A21), (B11 + B12))
        P1, P2, P3, P4, P5, P6, P7 = (rec_matrix_strassen(A11, S1),
                                      rec_matrix_strassen(S2, B22),
                                      rec_matrix_strassen(S3, B11),
                                      rec_matrix_strassen(A22, S4),
                                      rec_matrix_strassen(S5, S6),
                                      rec_matrix_strassen(S7, S8),
                                      rec_matrix_strassen(S9, S10))
        
        C[:mid, :mid], C[:mid, mid:], C[mid:, :mid], C[mid:, mid:] = ( 
            (P5 + P4 - P2 + P6),
            (P1 + P2), (P3 + P4),
            (P5 + P1 - P3 - P7))
        return C

print(rec_matrix_strassen(M1, M2))
        

