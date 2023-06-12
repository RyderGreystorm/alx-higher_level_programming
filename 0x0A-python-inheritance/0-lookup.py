#!/usr/bin/python3

def lookup(obj):
    """
    lookup - provides the list of availabe attributes of an object
    Args:
        obj: object passed to function as params
    """
    return sorted([attr for attr in dir(obj)])
