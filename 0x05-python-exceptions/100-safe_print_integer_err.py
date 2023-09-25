#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    error = "Unknown format code 'd' for object of type 'str'"
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
        raise Exception(error)
    except Exception:
        sys.stderr.write("Exception: {}\n".format(error))
        return False


value = 89
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = -89
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = "School"
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))
