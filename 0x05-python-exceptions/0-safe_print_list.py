#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    sum = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
        print()
        return (x)
    except IndexError:
        for num in my_list:
            sum += 1
        print()
        return min(x, sum)
