#!/usr/bin/python3
"""Using urllib to interact with websites"""

import urllib.request
import urllib.error
import sys


def run():
    """Begin code execution"""
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as mess:
        print(f"Error code: {mess.code}")


if __name__ == '__main__':
    run()
