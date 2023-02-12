#!/usr/bin/python3
"""Only sub-classes"""


def inherits_from(obj, a_class):
    """function to identify if an object inherts from a specified class
    Args:
        obj: object
        a_class: specified class
    Return:
        True: obj is instance of a class that inherits from a_class
        False: obj is not instance of a class that inherits from a_class
    """
    if (isinstance(obj, a_class) is True and type(obj) is not a_class):
        return (True)
    else:
        return (False)
