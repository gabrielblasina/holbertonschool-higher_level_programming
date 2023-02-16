#!/usr/bin/python3
"""First Rectangle"""


from models.base import Base


class Rectangle(Base):
    """class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """__init__ method
        Args:
            width: Privat instance attribute
            height: Privat instance attribute
            x: Privat instance attribute
            y: Privat instance attribute
            id: Public instance attribute
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
