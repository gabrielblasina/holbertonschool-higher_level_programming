#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    add = 0
    if (len(argv) - 1) == 0:
        print("{}".format(add))
    else:
        for index in range(1, len(argv)):
            add += int(argv[index])
        print("{}".format(add))
