"""
Problem 3: 
a.	Given a square matrix n*n (rows=columns), 
the problem is to sort the given matrix by row. The matrix is sorted by row if:
•	All elements in a row are sorted in increasing order 
•	and for row ‘i’, where 1 <= i <= n-1, first element of row 'i' is greater 
than or equal to the last element of row 'i-1'.
"""
def sort_matrix_by_row(matrix):
    """
    Sorts the matrix by row
    Input
            9 5 1
            8 2 6
            4 7 3
    Output
            1 2 3 
            4 5 6 
            7 8 9
    """
    matrix_copy = matrix.copy()
    n = len(matrix)
    flattened_matrix = [item for sublist in matrix_copy for item in sublist]
    flattened_matrix.sort()
    for i in range(n):
        for j in range(n):
            matrix[i][j] = flattened_matrix[i*n+j]
        
    return matrix_copy

def sort_matrix_by_column(matrix):
    """
    Sorts the matrix by column
    Input
        9 5 1
        8 2 6
        4 7 3
    Output:
        1 4 7 
        2 5 8 
        3 6 9

    """
    matrix_copy = matrix.copy()
    n = len(matrix)
    flattened_matrix = [item for sublist in matrix_copy for item in sublist]
    flattened_matrix.sort()
    for i in range(n):
        for j in range(n):
            matrix[j][i] = flattened_matrix[i*n+j]
    return matrix_copy
