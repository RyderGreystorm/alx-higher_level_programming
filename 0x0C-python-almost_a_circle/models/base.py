#!/usr/bin/python3

"""This is the base class. It will serve as the ancetor"""


import json


class Base():
    """Base class definition"""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Instantiates objects of class Base
        """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        json string coversion function
        Arg:
            list_dictionaries: argument to be converted to json
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        clss method that saves json representation of objects to a file
        Args:
            list_obj: objects to be serialized and saved
        """
        filename = cls.__name__ + ".json"
        json_objs = []
        if list_objs is not None:
            json_objs = [obj.to_dictionary() for obj in list_objs]
        with open(filename, mode="w", encoding="utf-8") as f:
            f.write(cls.to_json_string(json_objs))
