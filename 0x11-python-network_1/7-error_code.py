#!/usr/bin/python3
"""Use requests package to make http requests"""
import requests
import sys


def run():
    """Begin code execution"""
    url = sys.argv[1]
    response = requests.get(url)
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)


if __name__ == '__main__':
    run()
