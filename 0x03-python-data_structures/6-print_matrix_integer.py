#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for n in matrix:
        for m in range(len(n)):
            print("{:d}".format(n[m]), end="")
            if m < (len(n) - 1):
                print(" ", end="")
        print()
