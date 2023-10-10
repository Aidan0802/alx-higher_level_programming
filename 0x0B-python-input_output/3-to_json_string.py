#!/usr/bin/python3
"""This module contains a function that return the
representation of JSON as an object (string)
"""
import json


def to_json_string(my_obj):
    """This function that returns the JSON representation
    of an object (string)

    Args:
        parm1: Object
    """

    json_string = json.dumps(my_obj)
    return json_string
