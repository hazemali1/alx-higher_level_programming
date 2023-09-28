#!/usr/bin/python3


def find_peak(list_of_integers):
    d = None
    for s in list_of_integers:
        if d is None or d < s:
            d = s
    return d