import pytest

from solution_tests import fizzbuzz, is_leap_year


@pytest.mark.parametrize(
    "year, leap", [(2024, True), (2023, False), (1900, False), (2000, True)]
)
def test_is_leap_year(year, leap):
    assert is_leap_year(year) is leap


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, "1"),
        (3, "Fizz"),
        (5, "Buzz"),
        (15, "FizzBuzz"),
        (30, "FizzBuzz"),
    ],
)
def test_fizzbuzz(n, expected):
    assert fizzbuzz(n) == expected
