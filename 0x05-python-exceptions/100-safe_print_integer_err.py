#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    message = "Unknown format code 'd' for object of type 'str'"
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
        raise ValueError(message)
    except ValueError as e:
        sys.stderr.write("Exception: {e}\n")
        return False
