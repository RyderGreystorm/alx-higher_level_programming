#!/usr/bin/python3
"""LockClass function restricts vrible creation"""


class LockedClass:
    """class creation"""
    __slot__ = ['first_name']

    def __setattr__(self, name, value):
        if name != 'first_name':
            raise AttributeError("'LockedClass' object has no attribute 'last_name'")
        self.__dict__[name] = value
