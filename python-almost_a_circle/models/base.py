#!/usr/bin/python3
"""First class Base"""


class Base:
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
