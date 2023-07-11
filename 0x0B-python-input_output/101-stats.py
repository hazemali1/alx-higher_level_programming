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
    for a in sys.stdin:
        if d == 10:
            print("File size: {}".format(s))
            for j in sorted(w):
                print("{}: {}".format(j, w[j]))
            d = 1
        else:
            d += 1
        a = a.split()
        try:
            s += int(a[-1])
        except Exception:
            pass
        try:
            if a[-2] in q:
                if w.get(a[-2], -1) == -1:
                    w[a[-2]] = 1
                else:
                    w[a[-2]] += 1
        except IndexError:
            pass
    print("File size: {}".format(s))
    for j in sorted(w):
        print("{}: {}".format(j, w[j]))
except KeyboardInterrupt:
    print("File size: {}".format(s))
    for j in sorted(w):
        print("{}: {}".format(j, w[j]))
    raise
