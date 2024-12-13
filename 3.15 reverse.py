def main():
    original_tuple = (10, 20, 30, 40, 50)

    print(f"Tuple: {','.join(map(str, original_tuple))}")

    reversed_tuple = original_tuple[::-1]
    print(f"Reverse order: {','.join(map(str, reversed_tuple))}")


if __name__ == '__main__':
    main()