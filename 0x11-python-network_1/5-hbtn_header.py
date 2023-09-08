#!/usr/bin/python3
"""Use requests package to make http requests"""
import requests
import sys


def run():
    """Begin code execution"""
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))


if __name__ == '__main__':
    run()
