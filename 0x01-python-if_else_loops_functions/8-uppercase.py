#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if 'a' <= i <= 'z':
            upper = chr(ord(i) - 32)
            print("{}".format(upper), end='')
        else:
            print(end=' ')
    print()
