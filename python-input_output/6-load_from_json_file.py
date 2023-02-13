#!/usr/bin/python3
"""JSON file to object"""
import json


def load_from_json_file(filename):
    """function to decode a JSON file
    Args:
        filename: name of the file
    """
    with open(filename, encoding='UTF8') as my_file:
        new_obj = json.loads(my_file.read())
        return (new_obj)
