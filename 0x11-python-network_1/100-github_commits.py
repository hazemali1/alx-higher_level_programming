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
    url = 'https://api.github.com/repos/{}/{}/commits'.format(sys.argv[2],
                                                              sys.argv[1])
    s = requests.get(url)
    count = 1
    for d in s.json():
        if count <= 10:
            count += 1
            print('{}: {}'.format(d['sha'], d['commit']['author']['name']))
