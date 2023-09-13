#!/usr/bin/python3
import sys

argv = sys.argv[1:]
argc = 0
length = len(argv)
if length > 0:
    print("{} argumets:".format(length))
    while argc < length:
        arg = argv[argc]
        print("{}: {}".format(argc + 1, arg))
        argc += 1
else:
    print("{} arguments:".format(length))
