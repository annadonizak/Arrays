tup = (50, 20, 40, 50, 30, 50)
value = 50


def main():
    print(f"Tuple: {','.join(map(str, tup))}")

    occurrences = tup.count(value)

    print(f"Value: {value}")
    print(f"Number of occurrences: {occurrences}")


if __name__ == '__main__':
    main()