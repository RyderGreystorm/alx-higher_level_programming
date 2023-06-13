#!/usr/bin/python3

def read_file(filename=""):
    """
    Read file from a text file and print content
    Args:
        filename: textfile passed as argument to the function
    Return:
        Nothing
    """
    with open(filename, encoding="utf-8") as f:
        f_read = f.read()
        print(f_read)
