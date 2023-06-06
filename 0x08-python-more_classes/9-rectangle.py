#!/usr/bin/python3

"""Adding __repr___"""


class Rectangle:
    """Rectangle Definition"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initializing method attributes"""
        self.width = width
        self.height = height
        """increment the number_of_instnaces value by 1"""
        type(self).number_of_instances += 1

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
            rec_str += str(self.print_symbol) * self.__width + "\n"
        return rec_str[:-1]

    def __repr__(self):
        """Representation of the rectangle object"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """deleting an object"""
        print("Bye rectangle...")
        """Decrement number_of_instances by one per every instance deletion"""
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return rect_1
        elif rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return (cls(size, size))
