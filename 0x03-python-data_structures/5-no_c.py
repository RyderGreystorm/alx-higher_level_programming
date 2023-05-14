#!/usr/bin/python3
def no_c(my_string):
    if isinstance(my_string, str):
        res = ''
        for char in my_string:
            if char != 'c' and char != 'C':
                res += char
        return res
