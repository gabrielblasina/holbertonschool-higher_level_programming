#!/usr/bin/python3
"""inherits from a list"""


class MyList(list):
    """Subclass that inherits from list
    Args:
        list: superclass
    """
    def print_sorted(self):
        """public instance method
        Note:
            prints sorted list
        """
        sort_list = sorted(self)
        print(sort_list)
