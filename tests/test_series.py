import pytest

from series.series import fibonacci,lucas,sum_series

'''
fibonacci(0) == 0
fibonacci(1) == 1 
fibonacci(2) == 1 
fibonacci(3) == 2 
fibonacci(4) == 3 
etc.
'''
def test_zero():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected


def test_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected


def test_two():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected


def test_three():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected



'''
lucas(0) == 2
lucas(1) == 1 
lucas(2) == 3 
lucas(3) == 4 
lucas(4) == 7 
etc.
'''
def test_zero():
    actual = lucas(0)
    expected = 2
    assert actual == expected


def test_one():
    actual = lucas(1)
    expected = 1
    assert actual == expected


def test_two():
    actual = lucas(2)
    expected = 3
    assert actual == expected


def test_three():
    actual = lucas(3)
    expected = 4
    assert actual == expected



'''
sum_series(n) == n (first value)
sum_series(m) == m (secund value)
sum_series(x) == n + m 
sum_series(x) == (n + m) + m 
etc.
'''
def test_zero():
    actual = sum_series(0)
    expected = 0
    assert actual == expected

def test_one():
    actual = sum_series(1)
    expected = 1
    assert actual == expected

def test_two():
    actual = sum_series(2)
    expected = 1
    assert actual == expected

def test_three():
    actual = sum_series(3,2,2)
    expected = 6
    assert actual == expected

def test_four():
    actual = sum_series(4,3,2)
    expected = 12
    assert actual == expected