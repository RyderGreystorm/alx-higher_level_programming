#!/usr/bin/python3
def weight_average(my_list=[]):
    sum1, sum2 = 0, 0

    dic = dict(my_list)

    for key, value in dic.items():
        sum1 += key * value
        sum2 += value
    return sum1 / sum2
