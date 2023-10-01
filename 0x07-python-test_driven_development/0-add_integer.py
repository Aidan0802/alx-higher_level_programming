#!/usr/bin/python3
"""

This module consists of a function adds two number

"""


def add_integer(a, b=98):
    """ Function that calculates two numbers

    Args:
        parm1: First integer
        parm2: Second integer

    Raises:
        TypeError: If parm1 or parm2 are not integer/float

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    return a + b
