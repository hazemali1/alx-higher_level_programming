#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    s = {}
    for i, j in a_dictionary.items():
        s.update({i: j*2})
    return s
