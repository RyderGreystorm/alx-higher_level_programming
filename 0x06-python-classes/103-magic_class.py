#!/usr/bin/python3
"""MagicClass from Holberton."""

import math


class MagicClass:
    """Circle class"""

    def __init__(self, radius=0):
        """Initializing MagicClass object"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the area"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return The circumference"""
        return (2 * math.pi * self.__radius)
