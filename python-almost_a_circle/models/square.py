#!/usr/bin/python3
"""square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """class called Square wich inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """__init__ method
        Args:
            size: size of square
            x: x position of square
            y: y position of square
            id: optional id number
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """public instance method
        Returns:
            width
        """
        return (self.width)

    @property
    def size(self):
        """public instance method
        Returns:
            height
        """
        return (self.height)

    @size.setter
    def size(self, value):
        """public instance method
        Args:
            value: value to be set
        """
        self.width = value
        self. height = value

    def __str__(self):
        """string representation of an object
        Return:
            string representation of an object
        """
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    def update(self, *args, **kwargs):
        """Function to update the rectangle
        Args:
            *args: no_keyword argument
            **kwargs: keyword argument
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
