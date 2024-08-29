# Create a 3x3 2D array filled with zeros
from pkg_resources import Environment


rows, cols = 4, 4
matrix = [[0 for _ in range(cols)] for _ in range(rows)]

matrix =[
    ['S','F','F''F'],
     ['F','H','F','H'],
     ['F','F','F','H'],
     ['H','F','F','G']
]


def environment(matrix):
    for row in matrix:
        for element in row:
            if element == 'F':
                return -0.1
            elif element == 'G':
                return 1
            elif element == 'H':
                return -1
    return 0  # Return 0 for all other states (e.g., 'S')



result = environment(matrix)
print(result)