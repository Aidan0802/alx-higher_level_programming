#!/usr/bin/python3
def safe_print_integer(value):
    try:
        as_int = int(value)
    raise TypeError()
        print("{:d}".format(as_int))
        return True
    except ValueError:
        return False
