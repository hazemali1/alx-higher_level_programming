#!/usr/bin/python3
"""
error
"""


if __name__ == "__main__":
    """
    main
    """
    import urllib.request
    import urllib.error
    import sys
    """
    import
    """
    try:
        with urllib.request.urlopen(sys.argv[1]) as d:
            print(d.read().decode("UTF-8"))
    except urllib.error.HTTPError as s:
        print('Error code:', s.code)
