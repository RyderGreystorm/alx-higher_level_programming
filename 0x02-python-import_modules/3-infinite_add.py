#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    args = sys.argv
    argc = len(args) - 1
    sum = 0

    for arg in range(argc):
        sum = sum + int(args[arg + 1])
    print(sum)
