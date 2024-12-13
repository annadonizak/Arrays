arr = [2, 3, 2, 5, 8, 1, 9, 8]


def get_unique(array):
    repeated_elements = set([x for x in arr if arr.count(x) > 1])
    return set(array) - repeated_elements


def main():
    print("Array:", ' '.join(map(str, arr)))
    print("Unique elements:", ' '.join(map(str, get_unique(arr))))
    

if __name__ == '__main__':
    main()