from test_largest1 import findlargest


def test_largest_case_1():
    assert findlargest(2, 3, 5) == 5


def test_largest_case_2():
    assert findlargest(4, 5, 6) == 6


def test_largest_case_3():
    assert findlargest(7, 8, 9) == 9
