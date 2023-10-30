#!/usr/bin/python3
"""

This module contains an class Square

"""
Rectangle = __import__('9-rectangle').BaseGeometry


class Square(Rectangle):
    """This class inherits from class Rectangle"""
    def __init__(self, size):
        """Initialize an instance"""
        super().__init__(size, size)
        self.__size = size
        self.integer_validator("size", size)

    def __str__(self):
        """Method returns a string format"""
        return f"[Square] {self.__size}/{self.__size}"