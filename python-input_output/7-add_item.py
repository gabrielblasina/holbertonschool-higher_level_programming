#!/usr/bin/python3
""" load, add and save
    function that adds arguments to a python list and then
    saves them in a .json file
"""

import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

my_list = sys.argv[1:]
my_file = 'add_item.json'
save_to_json_file(my_list, my_file)
load_from_json_file(my_file)
