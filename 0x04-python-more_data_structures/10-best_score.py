#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        d = 0
        for i, j in a_dictionary.items():
            if j > d:
                d = j
        for p, l in a_dictionary.items():
            if l == d:
                return p
    else:
        return None
