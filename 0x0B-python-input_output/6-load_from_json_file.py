#!/usr/bin/python3
import json
"""create a python object from a JSON"""


def load_from_json_file(filename):
    """
    create a python object from JSON in a file
    Args:
        filename:file containing json
    Return: the python object
    """
    with open(filename, encoding="utf-8")as f:
        return json.load(f)
