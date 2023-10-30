#!/usr/bin/python3
"""

This module contains a function is_same_class

"""

def is_same_class(obj, a_class):
    """If object is the exact instance of specified class
    return true
    """
    return type(obj) is a_class
