#!/usr/bin/python3
"""

This module contains an class Rectangle

"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This class inherits from class BaseGeometry"""

    def __init__(self, width, height):
        """Initialize an instance of class Rectangle"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/}self.__height}"

    def __repr__(self):
        return self.__str__()
