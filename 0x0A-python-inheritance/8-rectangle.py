#!/usr/bin/python3
"""

This module contains an class Rectangle

"""


class Rectangle(BaseGeometry):
    """This class inherits from class BaseGeometry"""

    def __init__(self, width, height):
        """Initialize an instance of class Rectangle"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
