#!/usr/bin/python3
"""

This module contains a function that 
returns the list of available attributes and methods of an object

"""


def lookup(obj):
    """Looks up and returns the the list of available attributes 
    and methods of an object

    Args:
        parm1: Object
    """
    attrs_and_methods = dir(obj)
    filtered = [item for item in attrs_and_methods if not item.startswith("__")]
    return filtered

