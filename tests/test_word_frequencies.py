from functions import word_frequencies


def test_to_be():
    assert word_frequencies('To be or not to be') == {
        'to': 2, 'be': 2, 'or': 1, 'not': 1}


def test_punctuation_and_case():
    assert word_frequencies('Hello, hello!') == {'hello': 2}


def test_empty_string():
    assert word_frequencies('') == {}


def test_same_word_different_case():
    assert word_frequencies('Python Python python') == {'python': 3}


def test_polish_sentence_with_punctuation():
    assert word_frequencies('Ala ma kota, a kot ma Ale.') == {
        'ala': 1, 'ma': 2, 'kota': 1, 'a': 1, 'kot': 1, 'ale': 1}
