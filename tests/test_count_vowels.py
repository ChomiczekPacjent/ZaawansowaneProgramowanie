from functions import count_vowels


def test_python():
    assert count_vowels('Python') == 2


def test_all_uppercase_vowels():
    assert count_vowels('AEIOUY') == 6


def test_no_vowels():
    assert count_vowels('bcd') == 0


def test_empty_string():
    assert count_vowels('') == 0


def test_polish_chars():
    # Pró-ba żół-wia: ó, a, ó, i, a -> 5 samogłosek (z polskim "ó")
    assert count_vowels('Próba żółwia') == 5
