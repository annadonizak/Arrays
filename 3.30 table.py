def create_mul_table(rows, cols):
    array = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            array[i][j] = (i + 1) * (j + 1)

    return array


def main():
    table = create_mul_table(5, 5)

    for row in table:
        print("\t".join(map(str, row)))


if __name__ == '__main__':
    main()