#!/usr/bin/python3
"""Square #1"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """subclass Square that inherits from subclass Rectangle"""

    def __init__(self, size):
        """__init__ method
        Note:
            arg is validated by integer_validator
        Args:
            size: (private attribute) size of square
        """
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)
        self.__width = size
        self.__height = size

    def area(self):
        """area method
        Return:
            area of square
        """
        return (self.__width ** 2)
