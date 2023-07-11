#!/usr/bin/python3
"""
Log parsing
"""
import sys


s = 0
d = 0
w = {}
q = ['200', '301', '400', '401', '403', '404', '405', '500']
try:
    for i in sys.stdin:
        if d == 10:
            print("File size: {}".format(s))
            for j in sorted(w):
                print("{}: {}".format(j, w[j]))
            d = 1
        else:
            d += 1
        a = line.split()
        x = a[-2]
        try:
            s += int(a[-1])
        except Exception:
            pass
        try:
            if x in q:
                if w.get(x, -1) == -1:
                    w[x] = 1
                else:
                    w[x] += 1
        except Exception:
            pass
    print("File size: {}".format(s))
    for j in sorted(w):
        print("{}: {}".format(j, w[j]))
except KeyboardInterrupt:
    print("File size: {}".format(s))
    for j in sorted(w):
        print("{}: {}".format(j, w[j]))
    raise
