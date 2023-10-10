#!/usr/bin/python3
"""

This module contains a function that writes to a file

"""


def write_file(filename="", text=""):
    """This function writes data to a file
    Args:
        parm1: Filename to be written in
        parm2: Text to be written to file
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
    return len(text)
