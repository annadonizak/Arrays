rows = 3
cols = 5


def create_2d_array(x, y):
    array = []
    for _ in range(x):
        row = [0] * y
        array.append(row)
    return array


def main():
    array = create_2d_array(rows, cols)
    for row in array:
        print(row)


if __name__ == '__main__':
    main()