#!/usr/bin/python3
"""

This module contains an class Square

"""
Rectangle = __import__('9-rectangle').BaseGeometry


class Square(Rectangle):
    """This class inherits from class Rectangle"""
    def __init__(self, size):
        """Initialize an instance"""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """Method that return the area"""
        return self.__size * self.__size

    def __str__(self):
        """Method that return string"""
        return f"[Square] {self.__size}/{self.__size}"
