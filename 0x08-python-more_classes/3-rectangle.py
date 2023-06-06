#!/usr/bin/python3

"""String represenatation of rec"""


class Rectangle:
    """Rectangle Definition"""

    def __init__(self, width=0, height=0):
        """initializing method attributes"""
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """Set value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Finding the erea of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """perimeter calculation"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.width)

    def __str__(self):
        """String representation of rectangle"""
        if self.__height == 0 or self.__width == 0:
            return ""
        rec_str = ""
        for _ in range(self.__height):
            rec_str += "#" * self.__width + "\n"
        return rec_str[:-1]
