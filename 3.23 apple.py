import my_text

text = "An apple a day keeps the doctor away"


def main():
    num_words = my_text.word_count(text)
    words_longest_to_shortest = my_text.words_longest_to_shortest(text)
    words_alphabetically = my_text.words_alphabetically(text)

    print(f"Text: {text}")
    print(f"Number of words: {num_words}")
    print(f"Words from the longest: {', '.join(words_longest_to_shortest)}")
    print(f"Words ordered alphabetically: {', '.join(words_alphabetically)}")


if __name__ == '__main__':
    main()