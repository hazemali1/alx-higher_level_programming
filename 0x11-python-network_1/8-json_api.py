#!/usr/bin/python3
"""
search
"""


if __name__ == "__main__":
    """
    main
    """
    import requests
    import sys
    """
    import
    """
    s = ""
    if len(sys.argv) > 1:
        s = sys.argv[1]
    q = {'q': s}
    s = requests.post('http://0.0.0.0:5000/search_user', data=q)
    if s is not json():
        print('Not a valid JSON')
    else:
        if len(s.json()) == 0:
            print('No result')
        else:
            print('[{}] {}'.format(s.json()['id'], s.json()['name']))
