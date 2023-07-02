#!/usr/bin/python3
"""

take list and divide number

"""


def matrix_divided(matrix, div):
    """
    divide a matrix and handle all error
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(r, list) for r in matrix) or
            not all((isinstance(e, int) or isinstance(e, float))
                    for e in [num for r in matrix for num in r])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(r) == len(matrix[0]) for r in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    q = []
    for n in matrix:
        s = []
        for j in n:
            x = j / div
            s.append(round(x, 2))
        q.append(s)
    return q
