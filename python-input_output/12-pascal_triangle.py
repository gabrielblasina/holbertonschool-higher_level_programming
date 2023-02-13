#!/usr/bin/python3
"""pascal triangle"""


def pascal_triangle(n):
    """pascal's triangle of size n
    Return:
        list of lists of integers representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    result = []
    current_row = [1]
    result.append(current_row)
    for i in range(1, n):
        previous_row = current_row
        current_row = [1]
        for j in range(1, i):
            current_row.append(previous_row[j-1] + previous_row[j])
        current_row.append(1)
        result.append(current_row)
    return result
