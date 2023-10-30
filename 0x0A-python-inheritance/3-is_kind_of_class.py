#!/usr/bin/python3
"""

This module contains a function is_kind_of_class

"""


def is_kind_of_class(obj, a_class):
    """If object is the exact instance of or inherit
    of specified class return true
    """
    return isinstance(obj, a_class)
