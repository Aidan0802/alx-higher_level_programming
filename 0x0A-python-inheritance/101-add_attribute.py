#!/usr/bin/python3
"""

This module contains a function add_attribute

"""


def add_attribute(obj, attr_name, attr_val):
    """This function adds an attribute"""

    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, attr_val)
