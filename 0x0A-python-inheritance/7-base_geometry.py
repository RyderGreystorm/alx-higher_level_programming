#!/usr/bin/python3
"""
Geometric class"""


class BaseGeometry:
    """
    Geomtric base class
    """
    def area(self):
        """ Area of the geometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """instance validator"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
