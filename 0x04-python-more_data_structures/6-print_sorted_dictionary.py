#!/usr/bin.python3
def print_sorted_dictionary(a_dictionary):
    dic = list(a_dictionary.keys())
    dic.sort()
    for key in dic:
        print("{}: {}".format(key, a_dictionary[key]))
