#!/usr/bin/python3
"""
define class
"""


class MyInt(int):
    """
    MyInt class
    """
    def __eq__(self, value):
        """
        ==
        """
        return super().__ne__(value)

    def __ne__(self, value):
        """
        !=
        """
        return super().__eq__(value)
