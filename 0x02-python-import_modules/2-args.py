#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv[1:]
    argc = 0
    length = len(argv)

    if length > 1:
        print("{} arguments:".format(length))
        while argc < length:
            arg = argv[argc]
            print("{}: {}".format(argc + 1, arg))
            argc += 1
    elif length == 1:
        print("{} argument:".format(length))
        print("{}: {}".format(length, argv[0]))
    else:
        print("{} arguments.".format(length))
