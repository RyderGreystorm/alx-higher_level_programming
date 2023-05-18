#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    sum1, sum2 = 0, 0

    dic = dict(my_list)

    for key, value in dic.items():
        sum1 += key * value
        sum2 += value
    return sum1 / sum2
