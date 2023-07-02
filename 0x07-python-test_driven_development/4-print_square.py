#!/usr/bin/python3
"""

take an integer then print #

"""


def print_square(size):
    """
    print square with #
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for s in range(size):
        for d in range(size):
            print('#', end="")
        print("")
