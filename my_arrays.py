from copy import deepcopy


def second_largest(arr):
    largest = arr[0]
    second_largest = 0
    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    return second_largest


def largest_smallest_diff(arr):
    smallest = largest = arr[0]
    for num in arr:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
    return largest - smallest


def median(arr):
    arr = deepcopy(arr)
    # bubble sort
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    mid = len(arr) // 2
    return arr[mid]


def min_max(arr):
    smallest = largest = arr[0]
    for num in arr:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
    return [smallest, largest]


def array_to_string(arr):
    return '-'.join(map(str, arr))