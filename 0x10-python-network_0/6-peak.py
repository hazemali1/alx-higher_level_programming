#!/usr/bin/python3
"""find peak"""


def find_peak(list_of_integers):
    """list of int"""
    if len(list_of_integers) == 0:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    if list_of_integers[0] > list_of_integers[1]:
        return list_of_integers[0]
    if list_of_integers[-1] > list_of_integers[-2]:
        return list_of_integers[-1]
    s = list_of_integers[1:-2]
    print(s)
    return find_peak(s)
