#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) >= 2:
        a1, a2 = tuple_a[:2]
        if a1 < 0:
            a1 = 0
        if a2 < 0:
            a2 = 0
    else:
        a1 = tuple_a[0] if len(tuple_a) >= 1 else 0
        a2 = tuple_a[1] if len(tuple_a) >= 2 else 0
    if len(tuple_b) >= 2:
        b1, b2 = tuple_b[:2]
        if b1 < 0:
            b1 = 0
        if b2 < 0:
            b2 = 0
    else:
        b1 = tuple_b[0] if len(tuple_b) >= 1 else 0
        b2 = tuple_b[1] if len(tuple_b) >= 2 else 0
    first = a1 + b1
    second = a2 + b2

    return (first, second)
