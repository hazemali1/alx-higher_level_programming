#!/usr/bin/python3
def uniq_add(my_list=[]):
    s = set(my_list)
    d = 0
    for i in s:
        d += i
    return d
