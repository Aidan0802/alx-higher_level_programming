#!/usr/bin/python3
"""

This module contains a class MyList
that inherits from a list

"""


class MyList(list):
    """Class that inherits from a list
    Args:
        None
    """
    def print_sorted(self):
        """Print list in ascending order"""
        self.sort()
        print(self)
