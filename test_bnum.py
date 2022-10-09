import pytest

import bnum
from bnum import b


def test_it_should_be_equal_to():
    assert b(0.5) == b(0.5)


def test_it_not_compare_equality_to_unbounded_number():
    with pytest.raises(TypeError):
        assert b(0.5) == 0.5


def test_it_should_be_not_equal_to():
    assert b(0.5) != b(0.4)


def test_it_not_compare_inequality_to_unbounded_number():
    with pytest.raises(TypeError):
        assert b(0.5) != 0.4


def test_it_should_be_greater_than():
    assert b(0.5) > b(0.4)


def test_it_not_compare_greater_than_to_unbounded_number():
    with pytest.raises(TypeError):
        assert b(0.5) > 0.4


def test_it_should_be_greater_than_or_equal_to():
    assert b(0.5) >= b(0.5)
    assert b(0.5) >= b(0.4)


def test_it_not_compare_greater_than_or_equal_to_unbounded_number():
    with pytest.raises(TypeError):
        assert b(0.5) >= 0.4


def test_it_should_be_less_than():
    assert b(0.4) < b(0.5)


def test_it_not_compare_less_than_to_unbounded_number():
    with pytest.raises(TypeError):
        assert b(0.5) < 0.6


def test_it_should_be_less_than_or_equal_to():
    assert b(0.5) <= b(0.5)
    assert b(0.5) <= b(0.6)


def test_it_not_compare_less_than_or_equal_to_unbounded_number():
    with pytest.raises(TypeError):
        assert b(0.5) <= 0.6


def test_it_should_bind_an_integer():
    assert bnum.bind(1) == b(0.5)


def test_it_should_bind_a_float():
    assert bnum.bind(10.0) == b(0.9090909090909091)


def test_it_should_unbind_a_bound_number():
    assert b(0.6).unbounded == 1.5
