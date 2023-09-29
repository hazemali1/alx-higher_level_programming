#!/usr/bin/python3
import urllib.request
import sys
"""
id
"""


with urllib.request.urlopen(sys.argv[1]) as s:
    d = s.headers.__dict__
    print(d['_headers'][-3][1])
