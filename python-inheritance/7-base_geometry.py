#!/usr/bin/python3
"""Geometry module"""


class BaseGeometry:
    """class BaseGeometry"""
    def area(self):
        """public instance method
        Raise:
            Exception: 'area() is not implemented'
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """public instance method
        Raise:
            TypeError: if value is different of int
            ValueError: if value is less or equal than 0
        """
        if (type(value) is not int):
            raise TypeError(f'{name} must be an integer')
        if (value <= 0):
            raise ValueError(f'{name} must be greater than 0')
