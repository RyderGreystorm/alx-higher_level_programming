#!/usr/bin/python3
"""Using urllib to interact with websites"""

import urllib.request


def run():
    """Begin code execution"""
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        data = response.read()
        print(
                "Body response:",
                f"\t- type: {type(data)}",
                f"\t- type: {data}",
                f"\t- utf8 content: {data.decode('utf-8')}",
                sep='\n'
                )


if __name__ == '__main__':
    run()
