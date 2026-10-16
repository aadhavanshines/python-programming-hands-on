import pytest

from discount import apply_discount


def test_ten_percent_off():
    assert apply_discount(50.0, 10) == 45.0


def test_rounds_to_cents():
    assert apply_discount(19.99, 15) == 16.99


def test_rejects_bad_percent():
    with pytest.raises(ValueError):
        apply_discount(10.0, 120)


def test_full_discount():
    assert apply_discount(10.0, 100) == 1.0  # the test is wrong
