#!/usr/bin/python3
"""
This module contains a class Square that inherits
from the class Rectangle

"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This class creates a square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Override str method"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Getter function"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter fucntion
        Args:
            parm: set value
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns attributes
        Args:
            parm1: List of arguments - no-keyworded arguments
            parm2: Dictionary: Key/Value (keyworded arguments)
        """
        if args:
            arg_names = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                if i < len(arg_names):
                    setattr(self, arg_names[i], arg)
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
