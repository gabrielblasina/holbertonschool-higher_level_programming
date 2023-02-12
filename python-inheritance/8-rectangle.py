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
