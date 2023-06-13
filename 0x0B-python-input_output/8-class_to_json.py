#!/usr/bin/python3
"""
function that returns the dictionary description
with simple data structure (list, dictionary, string,
integer and boolean) for JSON serialization of an object
"""

import json


def class_to_json(obj):
    """
    Description: deserialize a json object
    Args:
        obj: json object file
    returns: te deserialized json to python object
    """
    serialize_dic = {}

    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serialize_dic[key] = value
        else:
            serialize_dic[key] = str(value)
    return serialize_dic
