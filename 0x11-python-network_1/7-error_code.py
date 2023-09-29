#!/usr/bin/python3
"""
error
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
    d = requests.get(sys.argv[1])
    if d.status_code < 400:
        print(d.content.decode())
    else:
        print('Error code:', d.status_code)
