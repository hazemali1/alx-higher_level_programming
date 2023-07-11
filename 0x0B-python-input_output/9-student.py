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

    def to_json(self):
        """
        class to json
        """
        return self.__dict__
