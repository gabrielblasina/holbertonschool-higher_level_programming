#!/usr/bin/python3
"""Rectangle that inherits from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """__init__ method
        Note:
            integer_validator to validate if args are integers greatter than 0
        Args:
            width: (private atribute) width of rectangle
            height: (private atribute) height of rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("heigth", height)
        self.__width = width
        self.__height = height

    def area(self):
        """area method
        Return:
            area of rectangle
        """
        return (self.__width * self.__height)

    def __str__(self):
        """__str__ method
        Return:
            returns readable representation of the rectangle
        """
        return (f'[{type(self).__name__}] {self.__width}/{self.__height}')
