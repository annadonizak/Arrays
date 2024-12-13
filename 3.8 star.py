arr = [2, 6, 4, 9, 7]


def star(n):
    return '*' * n


def main():
    for i in arr:
        print(f'{i}: {star(i)}')
    

if __name__ == '__main__':
    main()