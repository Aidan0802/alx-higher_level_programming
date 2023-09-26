#!/usr/bin/python3
class Square:
    """Class Square that defines a square.
    """
    def __init__(self, size=0):
        """
        Initializes a new instance of Square class.

        Args: param1: The size of the Square.
        """
        self.__size = size

    def size(self):
        """Getter method for retrieving the size.
        Returns: int: Size of square
        """
        return self.__size

    def size(self, value):
        """Setter method for setting the size.
        Args:
            value: Size to set.
        Raises:
            TypeError: If value is not integer
            ValueError: if value is not >= to 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates and returns area of square
        
        Return: int: Area of square
        """
        return self.__size * self.__size






my_square = Square(89)
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

my_square.size = 3
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

try:
    my_square.size = "5 feet"
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))
except Exception as e:
    print(e)
