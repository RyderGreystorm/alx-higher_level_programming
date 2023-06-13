#!/usr/bin/python3

"""find instance of an object"""


def is_kind_of_class(obj, a_class):
    """
    checks the instance of a class
    Args:
    obj: object to be compared to a class
    a_class: clss to be compared to
    Returns: True if obj is instance of a_class else false
    """
    return True if isinstance(obj, a_class) else False
