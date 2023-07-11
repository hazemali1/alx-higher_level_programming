#!/usr/bin/python3
"""
define function
"""


def pascal_triangle(n):
    """
    pascal
    """
    if n <= 0:
        return []
    s = [[1]]
    d = 0
    while len(s) < n:
        w = [1]
        for i in range(d):
            w.append(s[d][i] + s[d][i + 1])
        w.append(1)
        s.append(w)
        d += 1
    return s
