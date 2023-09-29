#!/usr/bin/python3
"""
id
"""


if __name__ == "__main__":
    """
    main
    """
    import requests
    import sys
    """
    import module
    """
    s = requests.get(sys.argv[1])
    d = s.headers.__dict__
    q = d['_store']
    for k, v in q.items():
        if v[0] == 'X-Request-Id':
            print(v[1])
