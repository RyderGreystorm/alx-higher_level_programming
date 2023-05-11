#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = sys.argv
    argc = len(args) - 1

    if len(args) == 1:
        print(f"{0} arguments.")
    elif len(args) == 2:
        print("{} argument:".format(argc))
    else:
        print("{} arguments:".format(argc))

    for arg in range(argc):
        print("{}: {}".format(arg + 1, args[arg + 1]))
