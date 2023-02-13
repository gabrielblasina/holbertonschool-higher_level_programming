#!/usr/bin/python3
"""student to JSON"""


class Student:
    """class student that defines a student"""

    def __init__(self, first_name, last_name, age):
        """__init__ method
        Args:
            first_name: public instance atribute
            last_name: public instance atribute
            age: public instance atribute
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """public instance method
        Args:
            attrs: list of given attributes
        Return:
            dictionary representation of student class
        """
        if (isinstance(attrs, list) and
                all(isinstance(elements, str) for elements in attrs)):
            return (self.__dict__)
