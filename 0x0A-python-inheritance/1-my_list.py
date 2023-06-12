#!/usr/bin/python3

"""
MyList, a child class inheriting from list classs
"""


class MyList(list):
    """
    MyList is a class inheriting from list class
    """

    def print_sorted(self):
        """
        method prints the sorted list to the stdout
        """
        sorted_list = sorted(self)
        print(sorted_list)
