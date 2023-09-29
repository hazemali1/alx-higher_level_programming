#!/usr/bin/python3
from urllib.request import urlopen
"""
What's my status
"""


with urlopen('https://alx-intranet.hbtn.io/status') as s:
    print('Body response:')
    print('\t- type:', type(s.read()))
with urlopen('https://alx-intranet.hbtn.io/status') as s:
    print('\t- content:', s.read())
with urlopen('https://alx-intranet.hbtn.io/status') as s:
    print('\t- utf8 content:', s.read().decode("UTF-8"))
