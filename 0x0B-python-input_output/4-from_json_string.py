#!/usr/bin/python3
"""This module contains a function that returns an
object (Python data structure) represented by a JSON string

"""
import json


def from_json_string(my_str):
    """Returns an object represented by 
    a JSON string

    Args:
        parm1: JSON string
    """
    parsed_data = json.loads(my_str)

    return parsed_data
