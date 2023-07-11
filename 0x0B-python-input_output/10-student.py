#!/usr/bin/python3
"""
define class
"""


class Student:
    """
    Student classes
    """
    def __init__(self, first_name, last_name, age):
        """
        init function
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        class to json
        """
        if (type(attrs) == list and
                all(type(e) == str for e in attrs)):
            return {s: getattr(self, s) for s in attrs if hasattr(self, s)}
        else:
            return self.__dict__
