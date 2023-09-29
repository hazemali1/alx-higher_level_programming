#!/usr/bin/python3
"""
github
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
    s = requests.get('https://api.github.com/user/repos', auth=(sys.argv[1],
                                                          sys.argv[2]))
    try:
        print(s.json()['id'])
    except KeyError:
        print(None)
