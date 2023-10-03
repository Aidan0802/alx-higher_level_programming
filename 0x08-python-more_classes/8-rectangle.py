#!/usr/bin/python3
"""

This module defines a Rectangle class

"""


class Rectangle:
    """ Class that defines Rectangle class
    Attributes:
        (int): Number of instances
        (str): Symbol to print as Rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initializes a new instance of Rectangle

        Args:
            width: Width of the rectangle
            height: Height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Caculates and returns the area"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """print the rectangle with the character #"""
        rectangle = ""
        if self.__height == 0 or self.__width == 0:
            return ""
        for _ in range(self.__height):
            rectangle += Rectangle.print_symbol * self.__width + "\n"
        return rectangle.rstrip()

    def __repr__(self):
        """Returns a string representation of the rectangle"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Decrements instance count and prints message"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...".format())

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area
        Args:
            parm1: Retangle instance 1
            parm2: Retangle instance 2
        Raises:
            TypeError: Must be an instance of Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return rect_1
        if rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2
