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

    @classmethod
    def save_to_file(cls, list_objs):
        """class method
        Note:
            Write json string of the list_objs into a file
        Args:
            cls: actual class
            list_objs: list of objects
        """
        filename = cls.__name__ + ".json"
        if list_objs is not None:
            list_dict = [obj.to_dictionary() for obj in list_objs]
        else:
            list_dict = []
        with open(filename, mode="w", encoding="utf-8") as file:
            file.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """static method
        Args:
            json_string: string representation of list of dictionaries
        Return:
            list represented by json_string
        """
        if json_string is None or json_string == "":
            return ([])
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """class method
        Args:
            cls: class
            **dictionary: dictionary
        Return:
            dummy: instance with all attributes set
        """
        if (cls.__name__ == "Rectangle"):
            dummy = cls(1, 1)
        elif (cls.__name__ == "Square"):
            dummy = cls(1)
        else:
            dummy = None
        dummy.update(**dictionary)
        return (dummy)
