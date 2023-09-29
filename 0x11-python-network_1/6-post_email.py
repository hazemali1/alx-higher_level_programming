#!/usr/bin/python3
"""
post
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
    email = {'email': sys.argv[2]}
    s = requests.post(sys.argv[1], data=email)
    print(s.content.decode())
