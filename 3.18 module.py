from my_arrays import *


def main():
    arr = [7, 3, 8, 5, 2]
    print(f"Numbers: {','.join(map(str, arr))}")
    print(f"Second largest number: {second_largest(arr)}")
    print(f"Median: {median(arr)}")
    print(f"Smallest and largest number: {','.join(map(str, min_max(arr)))}")
    print(f"Numbers as a string: {array_to_string(deepcopy(arr))}")


if __name__ == '__main__':
    main()