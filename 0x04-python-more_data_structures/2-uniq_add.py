#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    new_list = list(set(my_list))
    for num in new_list:
        sum += num
    return sum
