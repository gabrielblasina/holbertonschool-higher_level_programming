#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_list = [number if number != search else replace for number in my_list]
    return (my_list)
