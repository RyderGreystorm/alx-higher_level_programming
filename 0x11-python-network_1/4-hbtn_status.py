#!/usr/bin/python3
"""Use requests package to make http requests"""
import requests


def run():
    """Begin code execution"""
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    print(
            "Body response:",
            f"\t- type: {type(response.text)}",
            f"\t- content: {response.text}",
            sep='\n'
            )


if __name__ == '__main__':
    run()
