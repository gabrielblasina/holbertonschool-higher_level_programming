#!/usr/bin/python3
"""append to a file"""


def append_write(filename="", text=""):
    """function to append a string in text file and return chars added
    Args:
        filename: name of the file
        text: text to be append
    Return:
        number of characters appended
    """
    with open(filename, mode='a', encoding='UTF8') as my_file:
        return (my_file.write(text))
