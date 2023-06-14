#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    s = []
    for i in matrix:
        d = []
        for j in i:
            d.append(j**2)
        s.append(d)
    return s
