#!/usr/bin/python3
"""

This module contains a function that returns an
object (Python data structure) represented by a JSON string

"""
import json


def from_json_string(my_str):
    parsed_data = json.loads(my_str)

    return parsed_data
