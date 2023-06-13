#!/usr/bin/python3
"""Function converst a JSON object into a python object(data structure)"""


import json


def from_json_string(my_str):
    """
    Converst a JSON to python object
    Args:
        obj: json object
    Return: Returns the python object derived from the json
    """
    return json.loads(my_str)
