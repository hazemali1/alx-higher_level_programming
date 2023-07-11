#!/usr/bin/python3
"""
define function
"""
import json


def save_to_json_file(my_obj, filename):
    """
    save to json
    """
    with open(filename, "w") as s:
        json.dumps(my_obj, s)
