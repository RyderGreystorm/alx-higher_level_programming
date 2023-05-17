#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_arr = []
    for row in matrix:
        new_arr.append(list(map(lambda x: x ** 2, row)))
    return new_arr
