import pytest
from fib import *

def test_fib0():
    obs = fib(0)
    exp = 1
    assert obs == exp


def test_fib():
    obs = fib(1)
    exp = 1
    assert obs == exp

def test_fib5():
    obs = fib(5)
    exp = 8
    assert obs == exp

def test_fib_nonint():
    with pytest.raises(ValueError):
        obs = fib(2.5)

def test_fib_neg():
    with pytest.raises(ValueError):
        obs = fib(-1)

def test_fib_complex():
    with pytest.raises(TypeError):
        obs = fib(9+7j)
