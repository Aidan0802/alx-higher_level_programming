#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value

    for key in a_dictionary:
        print("{}: {}".format(key, a_dictionary[key]))

