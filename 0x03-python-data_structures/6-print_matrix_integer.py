#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        last = False
        for element in row:
            if element == row[-1]:
                last = True
            if last:
                print("{}".format(element), end="")
            else:
                print("{}".format(element), end=" ")
        print()
