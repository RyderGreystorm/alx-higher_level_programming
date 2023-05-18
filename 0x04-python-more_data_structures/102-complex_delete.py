#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    li = list(a_dictionary.keys())

    for var in li:
        if value == a_dictionary[var]:
            del a_dictionary[var]
    return a_dictionary
