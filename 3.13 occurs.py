arr = [15, 38, 7, 23, 14]


def occurs(number, array):
    return number in array


def main():
    number = int(input("Number: "))

    print("Array:", ' '.join(map(str, arr)))
    result = "appears" if occurs(number, arr) else "does not appear"
    print(f"Result: number {number} {result} in the array")


if __name__ == '__main__':
    main()