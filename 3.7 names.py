names = ['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']


def main():
    print(f'Names: {", ".join(names)}')

    longest_name = names[0]
    for name in names:
        if len(name) > len(longest_name):
            longest_name = name

    print(f'Longest name: {longest_name}')
    

if __name__ == '__main__':
    main()