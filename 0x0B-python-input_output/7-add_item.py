#!/usr/bin/python3
"""
define function
"""
import json
import sys
from os import path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if path.isfile("add_item.json"):
    my_list = load_from_json_file("add_item.json")
else:
    my_list = []
for s in sys.argv[1:]:
    my_list.append(s)
save_to_json_file(my_list, "add_item.json")
