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

    def __str__(self):
        """string representation of an object
        Return:
            string representation of an object
        """
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")
