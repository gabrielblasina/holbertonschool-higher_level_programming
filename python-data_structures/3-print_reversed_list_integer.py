#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_rev_list = my_list[::-1]
    for number in range(0, len(my_rev_list)):
        print("{:d}".format(my_rev_list[number]))
