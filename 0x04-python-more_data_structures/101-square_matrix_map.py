#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return (list(map(lambda d: list(map(lambda s: s ** 2, d)), matrix)))
