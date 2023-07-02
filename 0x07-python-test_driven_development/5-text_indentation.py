#!/usr/bin/python3
"""

take a strig and print it with some edits

"""


def text_indentation(text):
    """
    doing edit with ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    s = 0
    d = 0
    while s < len(text):
        if text[s] == '.' or text[s] == '?' or text[s] == ':':
            print(text[s], end="")
            print('\n')
            d = 1
        elif d == 1:
            d = 0
        elif d == 0:
            print(text[s], end="")
        s += 1
