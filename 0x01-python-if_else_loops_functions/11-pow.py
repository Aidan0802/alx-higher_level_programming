#!/usr/bin/python3
def pow(a, b):
    if a == 0:
        return 0
    if b == 0:
        return 1

    if b < 0:
        a = 1 / a
        b = -b

    res = 1
    for _ in range(b):
        res *= a
    return res
