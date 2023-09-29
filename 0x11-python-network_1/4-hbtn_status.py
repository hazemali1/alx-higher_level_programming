#!/usr/bin/python3
import requests


s = requests.get('https://alx-intranet.hbtn.io/status')
print('Body response:')
print('\t- type:', type(s.content.decode()))
print('\t- content:', s.content.decode())
