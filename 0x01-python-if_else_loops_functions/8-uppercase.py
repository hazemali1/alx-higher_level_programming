#!/usr/bin/python3
def uppercase(str):
    Str = ''
    for s in str:
        if ord(s) >= 97 and ord(s) <= 122:
            S = chr(ord(s) - 32)
        else:
            S = s
        Str += S
    print('{}'.format(Str))
