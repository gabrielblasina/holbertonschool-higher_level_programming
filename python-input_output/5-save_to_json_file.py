#!/usr/bin/python3
"""save JSON string to a file"""
import json


def save_to_json_file(my_obj, filename):
    """function writes an object to text file using JSON reptesentation
    Args:
        my_obj: object to convert
        filename: name of the file
    """
    with open(filename, mode='w', encoding='UTF8') as my_file:
        new_str = json.dumps(my_obj)
        my_file.write(new_str)
