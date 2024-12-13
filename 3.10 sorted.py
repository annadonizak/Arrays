arrays = [
    [64, 34, 25, 12, 22, 11, 90],
    [5, 2, 9, 1, 7, 6, 3],
    [38, 27, 43, 3, 9, 82, 10]
]


def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def main():
    for arr in arrays:
        print(f"Original: {arr}")
        print(f"Sorted:   {bubblesort(arr)}\n")
    

if __name__ == '__main__':
    main()