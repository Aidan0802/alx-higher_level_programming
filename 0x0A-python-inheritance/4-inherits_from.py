#!/usr/bin/python3
"""

This module contains a function inherits_from

"""


def inherits_from(obj, a_class):
    """If object inherits from a specified class
    return true
    """
    return type(obj) is not a_class and isinstance(obj, a_class)
