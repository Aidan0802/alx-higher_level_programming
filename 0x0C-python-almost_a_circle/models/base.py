#!/usr/bin/python3
"""

This module contains a class Base for managing id
attributes in future classes

"""
import json


class Base:
    """Base class for managing id attributes in future classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize an instance of class base
        Args:
            parm1: integer
        """
        if isinstance(id, int):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
