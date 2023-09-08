#!/usr/bin/python3
"""Using urllib to interact with websites"""

import urllib.request
import urllib.parse
import sys


def run():
    """Begin code execution"""
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    req = urllib.request.Request(url, data=data, method='POST')
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))


if __name__ == '__main__':
    run()
