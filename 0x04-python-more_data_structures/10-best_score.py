#!/usr/bin/python3
def best_score(a_dictionary):
    if isinstance(a_dictionary, dict):
        return max(a_dictionary, key=a_dictionary.get, default=None)
    else:
        return None
