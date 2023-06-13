#!/usr/bin/python3

"""Function writes to a file"""


def write_file(filename="", text=""):
    """
    Writes to a file
    Args:
        filename: file to which text must be written to
        text: text going into file
    """
    with open(filename, mode='w', encoding="utf-8") as f:
        num_words = f.write(text)
        return num_words
