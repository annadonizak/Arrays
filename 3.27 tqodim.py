array = [
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]

def main():
    for row in array:
        for item in row:
            print(item, end=" ")
        print()
    

if __name__ == '__main__':
    main()