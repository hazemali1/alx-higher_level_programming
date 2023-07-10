#!/usr/bin/python3
"""
define class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    rectangle class
    """
    def __init__(self, width, height):
        """
        init function
        """
        self.integer_validator("name", width)
        self.integer_validator("name", height)
        self.__width = width
        self.__height = height
