#!/usr/bin/python3
"""
define class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    square
    """
    def __init__(self, size):
        """
        init function
        """
        self.integer_validator("size", size)
        self.__size = size
