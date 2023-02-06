#!/usr/bin/python3
"""Defines a matrix division function."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix.
    Args:
        matrix (list): A list of lists of ints or floats.
        div (int/float): The divisor.
    Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.
    Returns:
        A new matrix representing the result of the division.
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if isinstance(div, (int, float)) is False:
        raise TypeError("div must be a number")
    if matrix is None:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    for lists in matrix:
        if isinstance(lists, list) is False:
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")
        if len(lists) == 0:
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")
        if len(lists) is not len(matrix[0]):
            raise TypeError("Each row of the matrix must have "
                            "the same size")
        for elmts in lists:
            if isinstance(elmts, (int, float)) is False:
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
    return [[round(elmts/div, 2) for elmts in lists] for lists in matrix]
