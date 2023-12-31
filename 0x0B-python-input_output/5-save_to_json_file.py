#!/usr/bin/python3
"""This module contains a function that writes an
Object to a text file, using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation

    Args:
        parm1: Python file
        parm2: File to be written to
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
