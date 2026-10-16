"""Small text statistics functions, tested in test_textstats.py."""


def word_count(text):
    return len(text.split())


def average_word_length(text):
    words = text.split()
    if not words:
        return 0.0
    letters = sum(len(word.strip(".,!?;:")) for word in words)
    return letters / len(words)


def reading_time_minutes(text, words_per_minute=200):
    """Whole minutes to read text, rounded up; at least 1 for any text."""
    words = word_count(text)
    if words == 0:
        return 0
    return -(-words // words_per_minute)
