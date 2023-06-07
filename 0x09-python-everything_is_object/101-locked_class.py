#!/usr/bin/python3
"""LockClass function restricts vrible creation"""


class LockedClass:
    """class creation"""
    __slot__ = ['first_name']
