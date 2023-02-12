#!/usr/bin/python3
"""from JSON string to object"""
import json


def from_json_string(my_str):
    """function that returns an object
    Args:
        my_str: str to convert
    Return:
        an object
    """
    new_obj = json.loads(my_str)
    return (new_obj)
