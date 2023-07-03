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
        print("Nshould be int")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N should be aleast 4")
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
