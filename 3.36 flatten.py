matrices = (
    [[2, 3],
     [1, 5]],
    [[5, 0, 3, 7, 5],
     [9, 0, 9, 1, 2]],
    [[2, 1],
     [3, 5],
     [7, 4],
     [2, 6]]
)


def flatten_matrix(matrix):
    return [item for row in matrix for item in row]


def print_matrix(matrix):
    for row in matrix:
        print(' '.join([str(i) for i in row]))


def print_array(array):
    print(' '.join([str(i) for i in array]))


def main():
    for matrix in matrices:
        print('Original matrix:')
        print_matrix(matrix)

        print('Flat matrix:')
        print_array(flatten_matrix(matrix))
        print()


if __name__ == '__main__':
    main()