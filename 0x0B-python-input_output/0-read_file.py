#!/usr/bin/python3
"""
define function
"""


def read_file(filename=""):
    """
    read file
    """
    with open(filename, encoding="utf-8") as s:
        print(s.read()), end=""
