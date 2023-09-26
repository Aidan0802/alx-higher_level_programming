#!/usr/bin/python3


class Square:
    """Class Square that defines a square
    """
    def __init__(self, size=0):
        """
        Initializes a new instance of Square class

        Args: param1: The size of the Square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        def cal_area(self):
            """Calculates and returns area of square
            
            Return: int: Area of square
            """
            return self.__size * self.__size

