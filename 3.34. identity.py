##Zadanie polega na stworzeniu funkcji, 
# która generuje macierz jednostkową 
##
n_sizes = [3, 5, 8]


def identity_matrix(n):   #gen macierz jednos
    matrix = [[0 for _ in range(n)] for _ in range(n)] #nxn wart=0

    for i in range(n): #iterujemy po indeks 0 do n-1
        matrix[i][i] = 1  #ust 1 na przekatnej macierzy
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(' '.join([str(i) for i in row])) #laczy w jeden ciag


def main():  #list wymiar mcierzy
    for n in n_sizes:
        matrix = identity_matrix(n) #twozrysz m jedn 
        print_matrix(matrix)
        print()


if __name__ == '__main__':
    main()