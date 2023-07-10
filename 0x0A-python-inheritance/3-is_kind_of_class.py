#!/usr/bin/python3
"""
taking two element
"""


def is_kind_of_class(obj, a_class):
    """
    check the type
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
