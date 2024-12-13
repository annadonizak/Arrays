matrices = ([
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
            ],
            [
                [1, 2, 3, 4, 5],
                [6, 7, 8, 9, 0]
            ],
            [
                [5, 6, 7, 8]
            ]
)


def transpose_matrix(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

    # # same with for loop
    # transposed = []
    # for i in range(len(m[0])):
    #     transposed_row = []
    #     for j in range(len(m)):
    #         transposed_row.append(m[j][i])
    #     transposed.append(transposed_row)
    # return transposed


def print_matrix(matrix):
    for row in matrix:
        print(' '.join([str(i) for i in row]))


def main():
    for matrix in matrices:
        print('Original matrix:')
        print_matrix(matrix)

        print('Transposed matrix:')
        print_matrix(transpose_matrix(matrix))
        print()


if __name__ == '__main__':
    main()