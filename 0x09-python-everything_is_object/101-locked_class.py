#!/usr/bin/python3
"""LockClass function restricts vrible creation"""


class LockedClass:
    """
    restricts user to useonly a specific attribute
    to set name
    """
    __slot__ = ["first_name"]
