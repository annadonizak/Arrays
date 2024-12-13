matrix = [
   [0, 0, 0],
   [0, 0, 0],
   [0, 0, 0]
]


for i in range(len(matrix)):
    matrix[i][i] = 1


for row in matrix:
    print(' '.join(map(str, row)))