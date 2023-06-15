#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    a = a_dictionary.copy()
    for i, j in  a.items():
        if j == value:
            del a_dictionary[i]
    return a_dictionary
