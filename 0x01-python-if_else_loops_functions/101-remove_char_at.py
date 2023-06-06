#!/usr/bin/python3
def remove_char_at(str, n):
    for w in str:
        if w != n:
            print(w, end='')
