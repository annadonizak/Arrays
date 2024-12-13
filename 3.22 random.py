import random

arr = [10, 20, 30, 40, 50]


def rand_elem(array):
    return random.choice(array)


def main():
    print("Random selection:", rand_elem(arr))


if __name__ == '__main__':
    main()