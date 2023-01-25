#!/usr/bin/python3
def max_integer(my_list=[]):
    if (my_list is None or not my_list):
        return (None)
    max_number = my_list[0]
    for number in my_list:
        if (max_number < number):
            max_number = number
    return (max_number)
