#!/usr/bin/python3
"""
No module imported
"""


class Square:
    """
    class that defines a square
    """
    def __init__(self, size=0):
        """
        __init__ method
        Notes:
            if size is not integer TypeError is raised
            if size is less than 0 ValueError is raised
        Args:
            size: Private atribute
        """
        if (type(size) != int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
