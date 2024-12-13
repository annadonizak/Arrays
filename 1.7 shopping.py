###
# Prints shopping list
#
def print_list():
    shopping_list = [
        "milk", "bread", "eggs", "butter", "cheese",
        "tomatoes", "potatoes", "carrots", "onions", "garlic"
    ]
    for item in shopping_list:
        print(item)


def main():
    print_list()


if __name__ == '__main__':
    main()