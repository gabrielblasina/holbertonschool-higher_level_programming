#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    counter = 0
    for rows in matrix:
        for counter, number in enumerate(rows):
            if (counter == (len(rows) - 1)):
                print("{:d}".format(number), end='')
            else:
                print("{:d}".format(number), end=' ')
        print()
