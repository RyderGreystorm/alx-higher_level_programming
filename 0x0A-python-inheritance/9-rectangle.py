#!/usr/bin/python3
"""Implementing the area"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class taht inherits fom the geometry class"""

    def __init__(self, width, height):
        """
        instanciating object an validating arguments passed to it
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str()  of a Rectangle."""
        str_g = "[" + str(self.__class__.__name__) + "] "
        str_g += str(self.__width) + "/" + str(self.__height)
        return str_g
