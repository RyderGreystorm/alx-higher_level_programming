#!/usr/bin/python3

"""
Find if an object is the instance of a class
"""


def is_same_class(obj, a_class):
    """
    Returns True if it is an object of a_class else False
    Args:
        obj: object of  a class
        a_class: class to which obj is being comapred
    """
    return type(obj) is a_class
