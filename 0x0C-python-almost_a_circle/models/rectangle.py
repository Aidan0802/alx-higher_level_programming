#!/usr/bin/python3
"""

This module contains a class Rectangle that
inherits from class Base

"""

from models.Base import Base

class Rectangle(Base):
    """ Inherits from class Bass
    Args:
        parm1: class Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize an instance of class Rectangle"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Getter function"""
        return self.__width
    @width.setter
    def width(self, value):
        """Setter function"""
        if not isinstance(value, int):
            raise TypeError("must be an integer")
        if value <= 0:
            raise ValueError("must be greater than 0")
        self.__width = value

    @property
    def height(self):
        """Getter function"""
        return self.__height
    @height.setter
    def height(self, value):
        """Setter function"""
        if not isinstance(value, int):
            raise TypeError("must be an integer")
        if value <= 0:
            raise ValueError("must be greater than 0")
        self.__height = value

    @property
    def x(self):
        """Getter function"""
        return self.__x
    @x.setter
    def x(self, value):
        """Setter function"""
        if not isinstance(value, int):
            raise TypeError("must be an integer")
        if value <= 0:
            raise ValueError("must be greater than 0")
        self.__x = value

    @property
    def y(self):
        """Getter function"""
        return self.__y
    @y.setter
    def y(self, value):
        """Setter function"""
        if not isinstance(value, int):
            raise TypeError("must be an integer")
        if value <= 0:
            raise ValueError("must be greater than 0")
        self.__y = value
