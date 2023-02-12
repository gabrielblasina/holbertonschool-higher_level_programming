#!/usr/bin/python3
"""Read a file"""


def read_file(filename=""):
    """Function that reads a file and print it to stdout
    Note:
        open, read and close the file
    Args:
        filename: name of file
    """
    with open(filename, encoding='UTF8') as my_file:
        print(my_file.read(), end='')
