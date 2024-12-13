arr = [
    [7, 3, 7, 9, 0],
    [2, 9, 0, 1, 5],
    [3, 8, 6, 4, 7],
    [8, 7, 1, 1, 5]
]


def last_col_sum(array):
    total = 0
    for row in arr:
        total += row[-1]
    return total


def main():
    print("Sum of the last column: ", last_col_sum(arr))


if __name__ == '__main__':
    main()