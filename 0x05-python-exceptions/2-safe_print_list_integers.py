#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    sum = 0
    try:
        for num in range(x):
            if isinstance(my_list[num], int):
                print("{:d}".format(my_list[num]), end="")
                sum += 1
        print()
        return sum
    except (ValueError, TypeError, IndexError):
        pass
