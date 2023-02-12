#!/usr/bin/python3
"""same class or is inherit"""


def is_kind_of_class(obj, a_class):
    """function to identify if obj is same class of inherits from a_class
    Args:
        obj: object
        a_class: the specified class
    Return:
        True: obj is same class or inherits from a_class
        False: obj is not same class or inherits from a_class
        """
    return (issubclass(type(obj), a_class))
