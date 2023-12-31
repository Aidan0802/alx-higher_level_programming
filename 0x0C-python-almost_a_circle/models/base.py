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

    @classmethod
    def load_from_file(cls):
        """Returns list of instances"""
        filename = f"{cls.__name__}.json"

        try:
            with open(filename, 'r') as file:
                json_string = file.read()
                dictionaries = cls.from_json_string(json_string)
                instances = [cls.create(**dic) for dic in dictionaries]
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes the CSV string representation of list_objs to a file
        Args:
        list_objs: List of instances that inherit from Base
        """
        filename = f"{cls.__name__}.csv"

        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
        for obj in list_objs:
            if cls.__name__ == "Rectangle":
                data = [obj.id, obj.width, obj.height, obj.x, obj.y]
            elif cls.__name__ == "Square":
                data = [obj.id, obj.size, obj.x, obj.y]
            writer.writerow(data)

    @classmethod
    def load_from_file_csv(cls):
        """Returns a list of instances from the CSV file"""
        filename = f"{cls.__name__}.csv"
        instances = []

        try:
            with open(filename, 'r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        id, width, height, x, y = map(int, row)
                        instance = cls(width, height)
                        instance.id = id
                        instance.x = x
                        instance.y = y
                    elif cls.__name__ == "Square":
                        id, size, x, y = map(int, row)
                        instance = cls(size)
                        instance.id = id
                        instance.x = x
                        instance.y = y
                    instances.append(instance)
                return instances
        except FileNotFoundError:
            return []
