#!/usr/bin/python3

"""Accepts an object and returns attribuutes of that object"""


def lookup(obj):
    """
    lookup - provides the list of availabe attributes of an object
    Args:
        obj: object passed to function as params
    """
    return dir(obj)
