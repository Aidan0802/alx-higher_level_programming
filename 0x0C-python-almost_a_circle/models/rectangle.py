#!/usr/bin/python3
"""

This module contains a class Rectangle that
inherits from class Base

"""


from models.base import Base


class Rectangle(Base):
    """ Inherits from class Bass
    Args:
        parm1: class Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize an instance of class Rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter function"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter function
        Args:
            parm: value to set
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter function"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter function
        Args:
            parm: value to set
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter function"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter function
        Args:
            parm: value to set
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter function"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter function
        Args:
            parm: value to set
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate and return the area"""
        return self.__height * self.__width
