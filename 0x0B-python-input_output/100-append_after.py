#!/usr/bin/python3
"""
define function
"""


def append_after(filename="", search_string="", new_string=""):
    """
    search and update
    """
    new = ""
    with open(filename) as s:
        for d in s:
            new += d
            if search_string in d:
                new += new_string
    with open(filename, "w") as q:
        q.write(new)
