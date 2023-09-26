#!/usr/bin/python3
"""
Define class Square
"""


class Square:
    """Class Square that defines a square
    """
    def __init__(self, size=0):
        """
        Initializes a new instance of Square class

        Args: param1: The size of the Square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
