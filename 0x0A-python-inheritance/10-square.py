#!/usr/bin/python3
"""Implementing the area"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square class"""

    def __init__(self, size):
        """Initialize a new square object

        Args:
            sizeof square pssed through validator
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
