#!/usr/bin/python3
"""
just firs name
"""


class LockedClass:
    """if user use any thing but first_name will get an error"""
    __slots__ = ["first_name"]
