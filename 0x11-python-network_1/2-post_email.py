#!/usr/bin/python3
"""
post
"""


if __name__ == "__main__":
    """
    main
    """
    import urllib.request
    import urllib.parse
    import sys
    """
    import
    """
    email = {'email': sys.argv[2]}
    d = urllib.parse.urlencode(email)
    s = urllib.request.Request(sys.argv[1], d.encode())
    with urllib.request.urlopen(s) as f:
        print(f.read().decode("UTF-8"))
