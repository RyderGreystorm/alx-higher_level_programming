#!/usr/bin/python3
"""function that reads file and prints its content to the standard output"""


def read_file(filename=""):
    """
    Read file from a text file and print content
    Args:
        filename: textfile passed as argument to the function
    Return:
        Nothing
    """

    with open(filename, encoding="utf-8") as f:
        for text in f:
            print(text, end="")
