#!/usr/bin/pyton3
"""serialiation"""

import json


def to_json_string(my_obj):
    """
    converts a python object to JSON
    Args:
        my_obj: object to be comverted to JSON
    Return: the new json object
    """
    return json.dumps(my_obj)
