#!/usr/bin/python3
def uppercase(str):
    _str = ""
    for i in str:
        if 'a' <= i <= 'z':
            upper = chr(ord(i) - 32)
            _str += upper
        else:
            _str += i
    print("{}".format(_str))

uppercase("hello world")

