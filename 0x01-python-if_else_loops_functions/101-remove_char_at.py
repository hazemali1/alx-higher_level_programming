#!/usr/bin/python3
def remove_char_at(str, n):
    Str = ''
    for w in range(len(str)):
        if w != n:
            Str += w
        return Str
