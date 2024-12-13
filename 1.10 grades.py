###
# Prints test statistics
#

test_results = [
    False, True, False, True, True,
    True, True, False, True, True,
    False, True, True, True, False
]


def print_test_stats(stats):
    # calculates the number of test questions
    question_number = len(stats)

    # calculates the number of correct answers
    correct_answers = 0
    for answer in test_results:
        if answer:
            correct_answers += 1

    # calculates the number of incorrect answers
    incorrect_answers = 0
    for answer in test_results:
        if answer == False:
            incorrect_answers += 1

    # calculates the percentage of correct answers
    perc_correct = correct_answers / question_number

    print('TEST STATISTICS')
    print('===============')
    print('Number of questions:', question_number)
    print('Number of correct answers:', correct_answers)
    print('Number of incorrect answers:', incorrect_answers)
    print('Percentage of correct answers:', f"{perc_correct:.0%}")


def main():
    print_test_stats(stats=test_results)


if __name__ == '__main__':
    main()