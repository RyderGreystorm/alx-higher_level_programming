#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newDic = {}
    for key, value in a_dictionary.items():
        newDic[key] = value * 2
    return newDic
