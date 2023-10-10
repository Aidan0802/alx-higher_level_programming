#!/usr/bin/python3
"""This module contains a function that
returns the dictionary description with simple data structure
for JSON serialization of an object
"""


def class_to_json(obj):
    """Returns the dictionary description with simple data
    structure for JSON
    Args:
        parm1: is an instance of a Class
    """
    if isinstance(obj, (int, str, bool)):
        return obj
    elif isinstance(obj, list):
        return [class_to_json(item) for item in obj]
    elif isinstance(obj, dict):
        return {key: class_to_json(value) for key, value in obj.items()}
    elif hasattr(obj, '__dict__'):
        return class_to_json(obj.__dict__)
    else:
        return None
