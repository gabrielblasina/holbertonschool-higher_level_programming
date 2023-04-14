#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return None
    [print('{:d}'.format(n)) for n in reversed(my_list)]
