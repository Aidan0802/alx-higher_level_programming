#!/usr/bin/python3
def best_score(a_dictionary):
    best = 0
    k = None
    if a_dictionary is not None:
        for key in a_dictionary:
            if a_dictionary[key] > best:
                best = a_dictionary[key]
                k = key
    return k
