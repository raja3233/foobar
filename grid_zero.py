from __future__ import division
def answer(matrix):
    # your code here
    row_list = matrix[:]
    column_list = [list(i) for i in zip(*matrix)]

    #for odd length of the matrix check row_sum and col_sum
    #This will eliminate non solvable problems.
    if len(row_list) % 2 :
        if not row_col_sum(row_list, column_list):
            return -1

    #Solvable problems
    #solve AX=B problem using Gaussian Elemination
    #Here A is Toggle Matrix(n*n * n*n), B =Given matrix
    #X is the  column matrix which store a value that each button clicked
    toggle_matrix = generate_toggel_matrix(len(matrix))
    puzzle_column = [item for row in matrix for item in row]
    diagonal_matrix, puzzle_column = gaussian_elimination(toggle_matrix, puzzle_column)
    c = sum(puzzle_column)
    return c


def gaussian_elimination(toggle_matrix, puzzle_matrix):
    """
    Returns Diagonal matrix and Transformed matrix of B in AX = B

    Guassian Elemination is done using pivoting concept
    After transfomation final matrices will be
    Toggle_Matrix   variable_matrix given_matrix(m)
    | 1 0 0 . . . 0 |    | x1 |     |m(0,0)|
    | 0 1 0 . . . 0 |    | x2 |     |m(0.1)|
    | 0 0 1 . . . 0 |  * | .. | =   |......|
    | . . . . . . . |    | .. |     |......|
    | 0 0 0 0 0 0 1 |    | xn |     |m(n,n)|
    """
    current_row = 0
    n = len(puzzle_matrix)
    for col in range(n):
        pivotRow = find_pivot(toggle_matrix, current_row, col, n)
        if pivotRow is None:
            continue

        swap(toggle_matrix, current_row, pivotRow)
        swap(puzzle_matrix, current_row, pivotRow)
        #for every non pivoting_row perform  row tranformation using power
        for row in range(n):
            if toggle_matrix[row][col]:
                if row != current_row:
                    for i in range(n):
                        toggle_matrix[row][i] ^= toggle_matrix[current_row][i]
                    puzzle_matrix[row] ^= puzzle_matrix[current_row]

        current_row += 1
    return toggle_matrix, puzzle_matrix


def find_pivot(toggle_matrix, start_row, col, n):
    """ returns non zero row at given col"""
    for row in range(start_row, n):
        if toggle_matrix[row][col]:
            return row
    return None

def swap(toggle_matrix, current_row, pivotRow):
    toggle_matrix[pivotRow], toggle_matrix[current_row] = toggle_matrix[current_row], toggle_matrix[pivotRow]

def generate_toggel_matrix(n):
    toggle_matrix = [[0] * n * n for i in range(n * n)]
    for i in range(n):
        for j in range(n):
            row = n * i + j
            for k in xrange(n):
                toggle_matrix[row][n * i + k] = 1
                toggle_matrix[row][n * k + j] = 1
    return toggle_matrix

def row_col_sum(row_list, column_list):
    """returns Ture ,given light parities for each row and column
       are same.
       i.e., sum of each individual row modulus 2 must be same
       and sum of each indiviual col modulus 2 must be same.
    """
    row_sum = sum(row_list[0]) % 2
    col_sum = sum(column_list[0]) % 2
    for row in row_list:
        if sum(row) % 2 != row_sum:
            return False
    for col in column_list:
        if sum(col) % 2 != col_sum:
            return False
    return True








