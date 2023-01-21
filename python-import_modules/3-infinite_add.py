#!/usr/bin/python3
import sys
if (__name__ == '__main__'):
    add = 0
    if ((len(sys.argv) - 1) == 0):
        print("{}".format(add))
    else:
        for index in range(1, len(sys.argv)):
            add += int(sys.argv[index])
        print("{}".format(add))
