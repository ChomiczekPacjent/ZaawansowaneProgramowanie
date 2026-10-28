from functions import flatten_list


def test_flat_list():
    assert flatten_list([1, 2, 3]) == [1, 2, 3]


def test_mixed_nesting():
    assert flatten_list([1, [2, 3], [4, [5]]]) == [1, 2, 3, 4, 5]


def test_empty_list():
    assert flatten_list([]) == []


def test_deep_single():
    assert flatten_list([[[1]]]) == [1]


def test_deep_chain():
    assert flatten_list([1, [2, [3, [4]]]]) == [1, 2, 3, 4]
