#!/usr/bin/python3
import sys

argv = sys.argv[1:]
argc = 0
while argc < len(argv):
    arg = argv[argc]
    print("{}: {}".format(argc + 1, arg))
    argc += 1
