#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv[1:]
    argc = 0
    arg_len = len(argv)
    result = 0

    while argc < arg_len:
        result += int(argv[argc])
        argc += 1

    print("{}".format(result))
