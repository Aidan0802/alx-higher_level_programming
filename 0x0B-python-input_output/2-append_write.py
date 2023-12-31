#!/usr/bin/python3
"""

This module contains a function that appends to the end of
a text file

"""


def append_write(filename="", text=""):
    """ This function appends to end of text file

    Args:
        parm1: Filename to append to
        parm2: Text to append
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
