def word_count(text):
    words = text.split()
    return len(words)


def words_longest_to_shortest(text):
    words = text.split()
    return sorted(words, key=len, reverse=True)


def words_alphabetically(text):
    words = text.split()
    return sorted(words)