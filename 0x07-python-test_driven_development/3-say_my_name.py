#!/usr/bin/python3
"""

This module consists of a print function

"""


def say_my_name(first_name, last_name=""):
    """ Prints my name is <first_name> <last_name>

    Args:
        parm1: string
        parm2: string

    Raises:
        TypeError: function parm must be a string

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}") 
