#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for co in row:
            print("{:d}".format(co), end=" " if co != row[-1] else "")
        print()
