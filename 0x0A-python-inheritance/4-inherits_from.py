#!/usr/bin/python3
"""
taking two element
"""


def inherits_from(obj, a_class):
    """
    check if obj is an instance of a class
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
