#!/usr/bin/python3
"""find peak"""


def find_peak(list_of_integers):
    """list of int"""
    max_i = None
    for ele in list_of_integers:
        if max_i is None or max_i < ele:
            max_i = ele
    return max_i
