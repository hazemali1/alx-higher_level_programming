#!/usr/bin/python3
"""
id
"""


if __name__ == "__main__":
    """
    main
    """
    import urllib.request
    import sys
    """
    import module
    """
    with urllib.request.urlopen(sys.argv[1]) as s:
        d = s.headers.__dict__
        print(d['_headers'][-3][1])
