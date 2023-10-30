#!/usr/bin/python3
"""

This module contains a class Rectangle
that inherits from 7-base_geometry


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
        """Method that calculate the area and return it

        """
        return self.__width * self.__height

    def __str__(self):
        """ Method that returns printable string

        """
        return f"[Rectangle] {self.__width}/}self.__height}"
