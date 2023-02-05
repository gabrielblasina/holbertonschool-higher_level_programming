#!/usr/bin/python3
"""
No module imported
"""


class Rectangle:
    """
    Class that defines a Rectangle
    """
    def __init__(self, width=0, height=0):
        """
        __init__ method
        Args:
            width: Private atribute
            height: Private atribute
        """
        self.width = width
        self.height = height

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
            value: private instance width's attribute
        """
        if (type(value) != int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
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
            value: private instance height's attribute
        """
        if (type(value) != int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if (self.__width == 0 or self.__height == 0):
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """
        __str__ method for string representation of an object
        Return:
            if width or height are 0, an empty string is returned
            return rectangle with '#'
        """
        print_rectangle = ''
        if (self.__width == 0 or self.__height == 0):
            return (print_rectangle)
        last_row = False
        for h in range(self.__height):
            if h == self.__height - 1:
                last_row = True
            print_rectangle += '#' * self.__width
            if (not last_row):
                print_rectangle += '\n'
        return (print_rectangle)

    def __repr__(self):
        """
        __repr__ method for string representation of object
        Return:
            string representation of the rectangle
        """
        return ('Rectangle({}, {})'.format(self.__width, self.__height))

    def __del__(self):
        """
        __del__ method deletes the instance
        Note:
            prints a message
        """
        print('Bye rectangle...')
