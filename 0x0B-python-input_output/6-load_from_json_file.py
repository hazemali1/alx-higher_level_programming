#!/usr/bin/python3
"""
define function
"""
import json


def load_from_json_file(filename):
    """
    obj from json file
    """
    with open(filename) as s:
        return json.load(s)
