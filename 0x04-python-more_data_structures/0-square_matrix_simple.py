#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [row[:] for row in matrix]

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            new_matrix[row][col] *= matrix[row][col]
    return new_matrix



matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)

