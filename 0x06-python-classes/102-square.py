#!/usr/bin/python3
"""Defining a Square class"""


class Square:
    """Square class"""

    def __init__(self, size=0):
        """Initializing new square object"""
        self.size = size

    @property
    def size(self):
        """Get/set size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return area of the square."""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """Define the == comparision of Squars"""
        return self.area() == other.area()

    def __ne__(self, other):
        """!= comparisonn of Squares"""
        return self.area() != other.area()

    def __lt__(self, other):
        """< comparison of  Squares"""
        return self.area() < other.area()

    def __le__(self, other):
        """<=   comparison to a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """comparison of  Squares"""
        return self.area() > other.area()

    def __ge__(self, other):
        """compmarison of Square"""
        return self.area() >= other.area()
