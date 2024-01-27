#!/usr/bin/python3

def matrix_divided(matrix, div):
    """Divides all elements of a matrix."""
    if not matrix or any(not row for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) \
                        of integers/floats")
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) \
                        of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    for i in matrix:
        if not isinstance(i, list):
            raise TypeError("matrix must be a matrix (list of lists) \
                            of integers/floats")
        elif len(i) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        else:
            for j in i:
                if not isinstance(j, (int, float)):
                    raise TypeError("matrix must be a matrix (list of lists) \
                                    of integers/floats")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    matrix_2 = [[round(j / div, 2) for j in i] for i in matrix]
    return matrix_2
