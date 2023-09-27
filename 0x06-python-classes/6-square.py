#!/usr/bin/python3
"""
Define class sqaure
"""


class Square:
    """Class Square that defines a square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of Square class.
        Args: param1: The size of the Square.
        """
        self.size = size
        self.position = position

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
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Method for retrieving the position.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Method for setting position
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(val, int) and val >= 0 for val in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Calculates and returns area of square
        Return: int: Area of square
        """
        return self.__size * self.__size

    def my_print(self):
        """Prints the square with the character '#'."""
        if self.__position == 0:
            print()
        elif self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
