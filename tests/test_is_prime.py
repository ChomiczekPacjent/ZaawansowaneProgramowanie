import pytest

from functions import is_prime


@pytest.mark.parametrize('n', [2, 3, 5, 97])
def test_primes(n):
    assert is_prime(n) is True


@pytest.mark.parametrize('n', [0, 1, 4])
def test_not_primes(n):
    assert is_prime(n) is False
