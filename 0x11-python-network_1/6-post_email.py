#!/usr/bin/python3
"""Use requests package to make http requests"""
import requests
import sys


def run():
    """Begin code execution"""
    url = sys.argv[1]
    email = sys.argv[2]
    response = requests.post(url, data={'email': email})
    print(response.text)


if __name__ == '__main__':
    run()
