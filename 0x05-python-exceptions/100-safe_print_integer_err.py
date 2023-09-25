#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    message = "Exception: Unknown format code 'd' for object of type 'str'"
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
        else:
            raise ValueError(message)
    except ValueError as error:
        sys.stderr.write(str(error))
        return False