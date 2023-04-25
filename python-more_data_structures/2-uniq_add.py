#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        return 0
    my_set = set(my_list)
    total = sum(my_set)
    return total
