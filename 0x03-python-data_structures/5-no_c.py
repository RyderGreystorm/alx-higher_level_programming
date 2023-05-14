#!/usr/bin/python3
def no_c(my_string):
    if isinstance(my_string, str):
        for index, char in enumerate(my_string):
            if char == 'c' or char == 'C':
                return my_string[:index] + my_string[index + 1:]
