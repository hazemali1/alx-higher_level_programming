#!/usr/bin/python3
"""
nqueens N
"""


import sys

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number\n")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4\n")
        sys.exit(1)
    s = []
    for i in range(int(sys.argv[1])):
        s.append([])
    d = 0
    for j in s:
        j.append(d)
        j.append(d)
        d += 1
    print(s)
