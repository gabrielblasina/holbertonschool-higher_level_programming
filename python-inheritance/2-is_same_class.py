#!/usr/bin/python3
"""instance of a specified class"""


def is_same_class(obj, a_class):
    """function to identify an object instance
    Note:
        identify if the object is exctly an instance of the specified class
    Args:
        obj: object
        a_class: the specified class
    Return:
        True: obj is exactly an instance of a_class
        False: obj is not exactly an instance of a_class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
