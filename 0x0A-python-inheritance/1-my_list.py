#!/usr/bin/python3
"""
making list
"""


class MyList(list):
    """
    creat list
    """
    def print_sorted(self):
        """
        sorted list
        """
        print(sorted(self))
