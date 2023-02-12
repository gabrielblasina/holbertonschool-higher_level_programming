#!/usr/bin/python3
"""write a file"""


def write_file(filename="", text=""):
    """function to write a string in text file and return chars written
    Args:
        filename: name of the file
        text: text to be written
    Return:
        number of characters written
    """
    with open(filename, mode='w', encoding='UTF8') as my_file:
        return (my_file.write(text))
