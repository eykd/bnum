import pickle

import pytest

import bnum
from bnum import b


def test_it_should_fail_to_construct_an_unbounded_number():
    with pytest.raises(ValueError):
        b(5)


def test_it_should_construct_a_bounded_number_from_a_bnum():
    assert b(b(0.5)) == b(0.5)


def test_it_should_bind_an_integer():
    assert bnum.bind(1) == b(0.5)


def test_it_should_bind_a_positive_float():
    assert bnum.bind(10.0) == b(0.9090909090909091)


def test_it_should_bind_a_negative_float():
    assert bnum.bind(-10.0) == b(-0.9090909090909091)


def test_it_should_unbind_a_bound_positive_number():
    assert b(0.6).unbounded == 1.5


def test_it_should_unbind_a_bound_negative_number():
    assert b(-0.6).unbounded == -1.5


def test_it_should_disallow_out_of_range_bounded_number():
    with pytest.raises(ValueError):
        b(1.1)


def test_it_should_convert_to_a_float():
    assert float(b(0.5)) == 0.5


def test_it_should_convert_to_a_str():
    assert str(b(0.5)) == "0.5"


def test_it_should_convert_to_a_repr_str():
    assert repr(b(0.5)) == "bnum(0.5)"


def test_it_should_pickle():
    result = pickle.loads(pickle.dumps(b(0.5)))
    assert result == b(0.5)


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


def test_it_should_add_bounded_numbers():
    result = b(0.5) + b(0.5)
    expected = b(0.6666666666666667)
    assert result == expected


def test_it_should_add_an_unbounded_number():
    result = b(0.5) + b(0.5).unbounded
    expected = b(0.6666666666666667)
    assert result == expected


def test_it_should_subtract_bounded_numbers():
    result = b(0.5) - b(0.5)
    expected = b(0.0)
    assert result == expected


def test_it_should_subtract_an_unbounded_number():
    result = b(0.5) - b(0.5).unbounded
    expected = b(0.0)
    assert result == expected


def test_it_should_multiply_bounded_numbers():
    result = b(0.6) * b(0.25)
    expected = b(0.33333333333333337)
    assert result == expected


def test_it_should_multiply_an_unbounded_number():
    result = b(0.6) * b(0.25).unbounded
    expected = b(0.33333333333333337)
    assert result == expected


def test_it_should_divide_bounded_numbers():
    result = b(0.6) / b(0.25)
    expected = b(0.8181818181818182)
    assert result == expected


def test_it_should_divide_an_unbounded_number():
    result = b(0.6) / b(0.25).unbounded
    expected = b(0.8181818181818182)
    assert result == expected


def test_it_should_exponent_bounded_numbers():
    result = b(0.6) ** b(0.25)
    expected = b(0.5337374181795533)
    assert result == expected


def test_it_should_exponent_an_unbounded_number():
    result = b(0.6) ** b(0.25).unbounded
    expected = b(0.5337374181795533)
    assert result == expected


def test_it_should_blend():
    result = b(0.5).blend(b(0.75), b(0.0))
    expected = b(0.6666666666666667)
    assert result == expected


@pytest.mark.parametrize(
    "x,expected", [(0.1, 0.3571428571428572), (-0.1, -0.3571428571428572)]
)
def test_it_should_amplify(x, expected):
    result = b(x).amplify()
    expected = b(expected)
    assert result == expected


@pytest.mark.parametrize(
    "x,weight,expected", [(0.1, 0.5, 0.4375), (-0.1, 0.5, -0.4375)]
)
def test_it_should_amplify_with_weight(x, weight, expected):
    result = b(x).amplify(weight)
    expected = b(expected)
    assert result == expected


@pytest.mark.parametrize(
    "x,expected", [(0.1, 0.052631578947368474), (-0.1, -0.052631578947368474)]
)
def test_it_should_suppress(x, expected):
    result = b(x).suppress()
    expected = b(expected)
    assert result == expected


@pytest.mark.parametrize(
    "x,weight,expected",
    [(0.1, 0.5, 0.027027027027026973), (-0.1, 0.5, -0.027027027027026973)],
)
def test_it_should_suppress_with_weight(x, weight, expected):
    result = b(x).suppress(weight)
    expected = b(expected)
    assert result == expected
