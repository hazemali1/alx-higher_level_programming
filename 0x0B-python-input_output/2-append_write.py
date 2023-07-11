#!/usr/bin/python3
"""
define function
"""


def append_write(filename="", text=""):
    """
    append write
    """
    with open(filename, "a", encoding="utf-8") as s:
        return s.write(text)
