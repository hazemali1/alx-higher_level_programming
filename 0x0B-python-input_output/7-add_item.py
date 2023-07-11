#!/usr/bin/python3
"""
define function
"""
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file
import json
import sys
from os import path


if path.isfile("add_item.json"):
    my_list = load_from_json_file("add_item.json")
else:
    my_list = []
for s in sys.argv[1:]:
    my_list.append(s)
save_to_json_file(my_list, "add_item.json")
