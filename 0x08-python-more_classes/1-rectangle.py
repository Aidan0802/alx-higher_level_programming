#!/usr/bin/python3
"""

This module defines a Rectangle class

"""


class Rectangle:
    """ Class that defines Rectangle class"""

    def __init__(self, width=0, height=0):
        """ Initializes a new instance of Rectangle

        Args:
            width: Width of the rectangle
            height: Height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getting width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the value of width
        Args:
            value: Value to set
        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getting height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the value of height
        Args:
            value: Value to set
        Raises:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value 
