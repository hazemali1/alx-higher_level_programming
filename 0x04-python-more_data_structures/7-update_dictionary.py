#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    s = {key: value}
    a_dictionary.update(s)
    return a_dictionary
