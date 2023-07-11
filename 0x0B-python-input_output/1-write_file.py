#!/usr/bin/python3
"""
define function
"""


def write_file(filename="", text=""):
    """
    write into file
    """
    with open(filename, "w", encoding="utf-8") as s:
        return s.write(text)
