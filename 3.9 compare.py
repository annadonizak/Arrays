# ARRAY = (["water", "book", "sky"], ["water", "book", "sky"])
# ARRAY = ([True, False], [True, False, True])
# ARRAY = ([5, 3, 1], [5, 3, 1])
ARRAY = ([3, 2, 1], [3, 2])


def compare(array1, array2):
    if len(array1) != len(array2):
        return 'arrays are different'

    for i in range(len(array1)):
        if array1[i] != array2[i]:
            return 'arrays are different'

    return 'arrays are the same'


def print_array(array):
    return ' '.join(map(str, array))


def main():
    print(f'Array1: {print_array(ARRAY[0])}')
    print(f'Array2: {print_array(ARRAY[1])}')
    print(f'Comparison: {compare(*ARRAY)}')


if __name__ == '__main__':
    main()