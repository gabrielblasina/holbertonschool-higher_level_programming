#!/usr/bin/python3
"""to JSON of string"""
import json


def to_json_string(my_obj):
    """function that return JSON representation of object
    Args:
        my_obj: object
    Return:
        JSON representation of an object
    """
    new_string = json.dumps(my_obj)
    return (new_string)
