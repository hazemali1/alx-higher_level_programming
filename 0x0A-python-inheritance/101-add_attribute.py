#!/usr/bin/python3
"""
function
"""


def add_attribute(my_obj, my_attr, my_value):
    """
    add_attribute
    """
    if not hasattr(my_obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(my_obj, my_attr, my_value)
