#!/usr/bin/python3
"""

This module contains a function add_attribute

"""


def add_attribute(obj, attr_name, attr_val):
    setattr(obj, attr_name, attr_val)

    if not hasattr(obj, attr_name) or getattr(obj, attr_name) != attr_val:
        raise TypeError("can't add new attribute if the object can't have new attribute")
