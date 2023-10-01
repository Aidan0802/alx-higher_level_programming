#!/usr/bin/python3
def matrix_divided(matrix, div):
    new_matrix = []
    error_1 = "matrix must be a matrix (list of lists) of integers/floats"
    error_2 = "Each row of the matrix must have the same size"
    first_row = len(matrix[0])
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list):
        raise TypeError(error_1)
    for row in matrix:
        if len(row) != first_row:
            raise TypeError(error_2)
        new_row = []
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError(error_1)
            result = round(elem / div, 2)
            new_row.append(result)
        new_matrix.append(new_row)

    return new_matrix
