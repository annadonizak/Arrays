n_sizes = [3, 5, 8]


def identity_matrix(n):   #gen macierz jednos
    matrix = [[0 for _ in range(n)] for _ in range(n)] #nxn wart=0

    for i in range(n):
        matrix[i][i] = 1  #ust 1 na przekatnej macierzy
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(' '.join([str(i) for i in row]))


def main():
    for n in n_sizes:
        matrix = identity_matrix(n)
        print_matrix(matrix)
        print()


if __name__ == '__main__':
    main()