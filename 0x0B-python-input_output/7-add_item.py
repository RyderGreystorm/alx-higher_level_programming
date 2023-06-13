#!/usr/bin/python3
"""script that adds arguments to a list"""


import sys
from os import path
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

args = sys.argv[1:]

path_file = 'add_item.json'

if path.exists(path_file):
    data = load_from_json_file(path_file)
else:
    data = []

data.extend(args)

save_to_json_file(data, path_file)
