arr = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]


def swap(array):
    for row in array:
        row[0], row[-1] = row[-1], row[0]


def main():
    print("Array before swapping:")
    for row in arr:
        print(row)

    swap(arr)

    print("\nArray after swapping:")
    for row in arr:
        print(row)


if __name__ == '__main__':
    main()