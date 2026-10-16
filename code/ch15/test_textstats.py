import pytest

from textstats import average_word_length, reading_time_minutes, word_count


def test_word_count_simple():
    assert word_count("the cat sat") == 3


def test_word_count_ignores_extra_spaces():
    assert word_count("  the   cat  ") == 2


def test_average_word_length_ignores_punctuation():
    assert average_word_length("Hi, you!") == 2.5


def test_average_word_length_of_empty_text():
    assert average_word_length("") == 0.0


@pytest.mark.parametrize(
    "words, minutes", [(0, 0), (1, 1), (200, 1), (201, 2), (1000, 5)]
)
def test_reading_time(words, minutes):
    text = "word " * words
    assert reading_time_minutes(text) == minutes
