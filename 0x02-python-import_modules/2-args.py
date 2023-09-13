#!/usr/bin/python3
import sys

args = sys.argv[1:]
argc = 1
for i in args:
    print("{}: {}".format(argc, i))
    argc += 1
