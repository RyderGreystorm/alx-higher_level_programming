#!/usr/bin/python3
"""
student class and json conversion
"""


class Student:
    """class definition"""
    def __init__(self, first_name, last_name, age):
        """instanciating other instances of the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary reperssetation of a student
        instance and returns it
        """
        if attrs is None:
            attrs = self.__dict__.keys()
        serialized_dic = {}

        for key, value in self.__dict__.items():
            if key in attrs:
                serialized_dic[key] = value

        return serialized_dic
