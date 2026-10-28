import pytest

from functions import calculate_discount


def test_twenty_percent():
    assert calculate_discount(100, 0.2) == 80.0


def test_no_discount():
    assert calculate_discount(50, 0) == 50.0


def test_full_discount():
    assert calculate_discount(200, 1) == 0.0


def test_negative_discount_raises():
    with pytest.raises(ValueError):
        calculate_discount(100, -0.1)


def test_discount_above_one_raises():
    with pytest.raises(ValueError):
        calculate_discount(100, 1.5)
