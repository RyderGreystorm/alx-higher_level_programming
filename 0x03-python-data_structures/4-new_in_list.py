#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if isinstance(my_list, list):
        var = my_list[:]
        if idx < 0:
            return var
        if idx >= len(my_list):
            return var
        else:
            var[idx] = element
            return var
