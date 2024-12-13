GAMES = [
    "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
    "League of Legends", "Valorant", "Grand Theft Auto V",
    "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]


def print_games(games):
    games_sorted = sorted(games)

    i = 0
    while i < len(games):
        print(f'{i + 1}: {games_sorted[i]}')
        i += 1


def main():
    print_games(games=GAMES)


if __name__ == '__main__':
    main()