#!/usr/bin/python3
def matrix_divided(matrix, div):
    if not isinstance(matrix, (list, float)):
        for mat in range(len(matrix)):
            if not isinstance(matrix[mat], (int, float)):
                if not isinstance(matrix[mat][mat], (int, float)):
                        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            else:
                row_length = len(matrix[0])
                if row_length != len(matrix[mat]):
                    raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        return list(map(lambda x : [round((i / div), 2) for i in x], matrix))
