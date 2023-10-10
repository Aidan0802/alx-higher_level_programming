#!/usr/bin/python3
"""

This module contains a function that read text file

"""


def read_file(filename=""):
    """Reads a file input
    Args:
        parm1: Textfile input
    """
    with open(filename, "r", encoding="utf-8") as file:
        read_data = file.read()
        print(read_data, end="")
