#!/usr/bin/python3

"""Instance of  class or not"""


def inherits_from(obj, a_class):
    """
    FInds the instance of a class
    Args:
    obj: the object being passed as an argument
    a_class: class being compared with the obj
    Returns: True if is it instance of the class or inherited from the class
    otherwise it prints False
    """
    return any(issubclass(type(obj), cls) for cls in a_class.__subclasses__())
