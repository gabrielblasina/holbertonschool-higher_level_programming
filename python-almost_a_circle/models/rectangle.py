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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        private instance method
        Note:
            returns the width
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        private instance method
        Note:
            value validation
        Args:
            value: private instance height's attribute
        """
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        private instance method
        Note:
            returns the height
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        private instance method
        Note:
            value validation
        Args:
            value: private instance width's attribute
        """
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        private instance method
        Note:
            returns the x
        """
        return (self.__x)

    @x.setter
    def x(self, value):
        """
        private instance method
        Note:
            value validation
        Args:
            value: private instance x's attribute
        """
        if isinstance(value, int) is False:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        private instance method
        Note:
            returns the y
        """
        return (self.__y)

    @y.setter
    def y(self, value):
        """
        private instance method
        Note:
            value validation
        Args:
            value: private instance y's attribute
        """
        if isinstance(value, int) is False:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Function to know the area of the rectangle
        Return:
            Return area of the rectangle
        """
        return (self.__height * self.__width)

    def display(self):
        """Function to display de rectangle"""
        for i in range(self.height):
            print("#" * self.width)
