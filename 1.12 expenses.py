categories = ["Food", "Transport", "Rent", "Entertainment"]
expenses = [500, 150, 1000, 200]


def get_most_expensive_cat(cats, exps):
    max_expense_index = expenses.index(max(exps))

    most_expensive_category = cats[max_expense_index]
    highest_expense = exps[max_expense_index]

    print(f"The most expensive category is {most_expensive_category} with an expense of ${highest_expense}")


def main():
    get_most_expensive_cat(categories, expenses)


if __name__ == '__main__':
    main()