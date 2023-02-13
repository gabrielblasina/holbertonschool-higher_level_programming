#!/usr/bin/python3
"""class to JSON"""


def class_to_json(obj):
    """function that returns dictionary description with simple data
    structure for JSON serialization of an object
    Args:
        obj: instance of a Class
    Return:
        dictionary description
    """
    return (obj.__dict__)
