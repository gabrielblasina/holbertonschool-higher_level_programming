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

    def area(self):
        """
        Public instance method
        Note:
            returns the current square area
        """
        return (self.__size * self.__size)

    @property
    def size(self):
        """
        private instance method
        Note:
            Returns the size
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        private instance method
        Note:
            value validation
        Args:
            value: private instance size's attribute
        """
        if (type(value) != int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """
        public instance method
        Note:
            print the square using '#'
            if the size es 0 a new line is printed
        """
        if (self.__size == 0):
            print()
        else:
            for row in range(self.__size):
                for column in range(self.__size):
                    print('#', end='')
                print()
