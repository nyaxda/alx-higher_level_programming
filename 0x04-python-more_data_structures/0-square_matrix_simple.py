#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return None
    else:
        matrix2 = [[x ** 2 for x in row] for row in matrix]
    return matrix2
