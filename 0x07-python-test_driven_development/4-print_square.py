#!/usr/bin/python3
"""

This module consist of a print function

"""


def print_square(size):
    """ This function prints a square of '#'

    Args:
        parm: size of the square

    Raises:
        TypeError: size must be an integer
        ValueError: size must be greater or equal to 0

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for row in range(size):
        for col in range(size):
            print("#", end="")
        print()
