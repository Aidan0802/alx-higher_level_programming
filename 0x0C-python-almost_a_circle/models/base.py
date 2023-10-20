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

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to file
        Args:
            parm: List of instances who inherits of Base
        """
        if list_objs is None:
            list_objs = []
        filename = f"{cls.__name__}.json"

        dictionaries = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(dictionaries)

        with open(filename, 'w') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation
        Args:
            parm: String representation of a list of dictionaries
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an instance with attrs set from dictionary
        Args:
            parm: Dictionary
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy
