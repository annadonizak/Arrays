arr = [7, 9, 2, 4, 5, 6]


def main():
    even_nums = [num for num in arr if num % 2 == 0]
    odd_nums = [num for num in arr if num % 2 != 0]

    result = even_nums + odd_nums

    print("Original array:", arr)
    print("Rearranged array:", result)
    

if __name__ == '__main__':
    main()