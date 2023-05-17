#!/usr/bin.python3
def print_sorted_dictionary(a_dictionary):
    dic = sorted(a_dictionary.keys())
    for key in dic:
        value = a_dictionary[key]
        print(f"{key}: {value}")
