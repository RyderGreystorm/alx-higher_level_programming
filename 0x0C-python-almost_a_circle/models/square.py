#!/usr/bin/python3
"""Class Squarei definition inheriting from Rectngle"""


from models.rectangle import Rectangle


class Square(Rectangle):

    """
    class definition for the square
    Args:
        Retangle: inheriting from rectangle class
    """

    def __init__(self, size, x=0, y=0, id=None):

        """
        initilizing the objects of class self and
        inheriting from class Rectangle
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):

        """String method for instnces of the class"""

        return "[square] ({}) {}/{} - {}".format(
                self.id,
                self.x,
                self.y,
                self.width)

    @property
    def size(self):
        """
        returns the value of size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        sets the value of the test
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        updates the class attributes
        Args:
            args: non keyworded arguments
            kwargs: keyworded arguments
        """
        if args and len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.__size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """
        converts object attributes to dictionary
        Returs: dictionary of the object
        """
        return {
                'id': self.id,
                'size': self.__size,
                'x': self.x,
                'y': self.y
                }
