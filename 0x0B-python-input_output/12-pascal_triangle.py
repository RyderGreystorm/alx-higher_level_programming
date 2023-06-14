#!/usr/bin/python3
"""Pascal traingle"""


def pascal_triangle(n):
    """
    generates the pascal triange
    Args:
        n: number of rows for the traingle
    Returns:
        The traingle
    """
    traingle = []
    if n <= 0:
        return traingle
    for i in range(n):
        row = [1] * (i + 1)
        if i > 1:
            for j in range(1, i):
                row[j] = traingle[i - 1][j - 1] + traingle[i - 1][j]
        traingle.append(row)
    return traingle
