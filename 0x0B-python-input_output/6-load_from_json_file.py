#!/usr/bin/python3
"""This module contains a function that
creates an Object from a JSON file
"""
import json


def load_from_json_file(filename):
    """Creates and Object from a JSON file
    Args:
        parm1: JSON string
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
