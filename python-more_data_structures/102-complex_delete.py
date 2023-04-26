#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary == {}:
        return a_dictionary
    dict_cpy = a_dictionary.copy()
    for k in dict_cpy.keys():
        if dict_cpy[k] == value:
            del a_dictionary[k]
    return a_dictionary
