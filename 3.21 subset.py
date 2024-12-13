arr1 = [1, 2, 3]
arr2 = [1, 2, 3, 4, 5]


def is_subset(arr1, arr2):
    return all(elem in arr2 for elem in arr1)


def main():
    print(f"{arr1} is subset of {arr2}: {is_subset(arr1, arr2)}")


if __name__ == '__main__':
    main()