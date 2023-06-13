#!/usr/bin/python3
"""Read from json and save"""


import json


def save_to_json_file(my_obj, filename):
    """
    resds from a json file and saves
   Args:
    my_obj: jsin object
    filename: file to save to
    """
    with open(filename, mode='w', encoding="utf-8") as f:
        json.dump(my_obj, f)
