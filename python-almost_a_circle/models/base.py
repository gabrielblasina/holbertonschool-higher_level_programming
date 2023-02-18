#!/usr/bin/python3
"""First class Base"""


import json


class Base:
    """class called Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """__init__ method
        Args:
            id: Publid instance attribute
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Static method
        Args:
            list_dictionaries: a list of dictionaries
        Return:
            JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        return (json.dumps(list_dictionaries))
