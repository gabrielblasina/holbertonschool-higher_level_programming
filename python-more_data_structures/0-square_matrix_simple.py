#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix1 = []
    new_matrix2 = []
    for rows in matrix:
        new_matrix1 = list(map(lambda value: value ** 2, rows))
        new_matrix2.append(new_matrix1)
    return new_matrix2
