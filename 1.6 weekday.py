###
# Returns the name of the day of the week for a given day number (1-Monday ... 7-Sunday)
#

def weekday(n):
    weekdays = ["Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"]

    if n < 1 or n > 7:
        raise ValueError("Invalid day number. Please enter a number between 1 and 7.")

    return weekdays[n - 1]


def main():
    for n in [1, 4, 7]:
        print(weekday(n))


if __name__ == '__main__':
    main()