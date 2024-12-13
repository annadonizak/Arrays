# 3x3 Tic-Tac-Toe board
tic_tac_toe_board = [
    ['X', 'O', 'X'],
    [' ', 'X', 'O'],
    ['O', ' ', 'X']
]


def print_board():
    for row in tic_tac_toe_board:
        for item in row:
            print(item, end=" ")
        print()


def main():
    print_board()


if __name__ == '__main__':
    main()