#!/usr/bin/python3
"""
Define class sqaure
"""


class Square:
    """Class Square that defines a square.
    """
    def __init__(self, size=0):
        """
        Initializes a new instance of Square class.
        Args: param1: The size of the Square.
        """
        self.size = size

    @property
    def size(self):
        """Getter method for retrieving the size.
        Returns: int: Size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for setting the size.
        Args:
            value: Size to set.
        Raises:
            TypeError: If value is not integer
            ValueError: if value is not >= to 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates and returns area of square
        Return: int: Area of square
        """
        return self.__size * self.__size

    def my_print(self):
        if self.__size > 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
