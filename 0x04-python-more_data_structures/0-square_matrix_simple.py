#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [row[:] for row in matrix]

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            new_matrix[row][col] *= matrix[row][col]
    return new_matrix
