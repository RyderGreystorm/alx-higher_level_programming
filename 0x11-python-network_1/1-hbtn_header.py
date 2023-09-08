#!/usr/bin/python3
"""Using urllib to interact with websites"""

import urllib.request
import sys


def run():
    """Begin code execution"""
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.headers['X-Request-Id'])


if __name__ == '__main__':
    run()
