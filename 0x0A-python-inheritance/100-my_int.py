#!/usr/bin/python3
"""

This module contains an class MyInt

"""


class MyInt(int):
    """This class inherits from int"""
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
