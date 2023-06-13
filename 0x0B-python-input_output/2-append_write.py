#!/usr/bin/python3
"""Append text to the file"""


def append_write(filename="", text=""):
    """
    append text to the file and if fil does not exist it is created
    args:
        filename:file to which text must be appended to
        text: content being appended to the file
    """
    with open(filename, mode='a', encoding="utf-8") as f:
        num = f.write(text)
        return num
