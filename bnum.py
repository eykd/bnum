"""bnum -- bounded numbers
"""
from __future__ import annotations

from typing import Optional, Union


def _bind(unbounded_number: Union[float, int]) -> float:
    """Transform an unbounded number into an bounded number."""
    if unbounded_number > 0.0:
        return 1.0 - (1.0 / (1.0 + unbounded_number))
    else:
        return (1.0 / (1.0 - unbounded_number)) - 1.0


def _unbind(bounded_number: float) -> float:
    """Transform a bounded number into an unbounded number."""
    if bounded_number > 0.0:
        return (1.0 / (1.0 - bounded_number)) - 1.0
    else:
        return 1.0 - (1.0 / (1.0 + bounded_number))


def bind(x) -> bnum:
    """Bind an unbounded number to a bnum value between -1 and 1.

    Note that in the world of bounded numbers, from ten on up, the
    number of places beyond 1 *roughly* corresponds to the number of
    nines.  That is:
        10 ~= 0.9
       100 ~= 0.99
      1000 ~= 0.999
       ...

    Note also that the journey from unbounded to bounded will result
    in rounding errors.  The larger the unbounded number, the larger
    the round-trip deviation.
    """
    return bnum(_bind(float(x)))


def unbounded(x: Union[bnum, float, int]) -> float:
    if isinstance(x, bnum):
        return x.unbounded
    else:
        return x


class bnum:
    """bnum(x) -> bounded floating point number

    Convert a string or number to a bounded floating point number, if possible.

    Don't try and get all devious and exact with bnums, or the
    rounding errors will eat your lunch.
    """

    value: float

    @property
    def unbounded(self):
        """Return the unbounded value.

        Note the journey from bounded to unbounded will result in
        rounding errors.  The larger the unbounded number, the larger
        the round-trip deviation.
        """
        return _unbind(self.value)

    @classmethod
    def _check_range(cls, x: float) -> None:
        if isinstance(x, cls):
            return x.value

        if x <= -1.0 or x >= 1.0:
            raise ValueError(f"Invalid value {x!r} for bnum")

        return x

    def __init__(self, value: float):
        self.value = self._check_range(value)

    def __add__(self, y: float) -> bnum:
        """x.__add__(y) <==> x+y"""
        y_ub = unbounded(y)
        return bind(self.unbounded + y_ub)

    def __truediv__(self, y: float) -> bnum:
        """x.__div__(y) <==> x/y"""
        y_ub = unbounded(y)
        return bind(self.unbounded / y_ub)

    def __float__(self) -> float:
        """x.__float__() <==> float(x)"""
        return float(self.value)

    def __mul__(self, y: float) -> bnum:
        """x.__mul__(y) <==> x*y"""
        y_ub = unbounded(y)
        return bind(self.unbounded * y_ub)

    def __pow__(self, y: float, mod: Optional[float] = None) -> bnum:
        """x.__pow__(y[, z]) <==> pow(x, y[, z])"""
        y_ub = unbounded(y)
        return bind(pow(self.unbounded, y_ub, mod))

    def __str__(self):
        """x.__str__() <==> str(x)"""
        return str(self.value)

    def __repr__(self):
        return f"bnum({self.value})"

    def __sub__(self, y: float):
        """x.__sub__(y) <==> x-y"""
        y_ub = unbounded(y)
        return bind(self.unbounded - y_ub)

    def __reduce__(self):
        return (bnum, (self.value,))

    def __eq__(self, y):
        """x == y"""
        if isinstance(y, bnum):
            return self.value == y.value
        else:
            raise TypeError("Can't compare bounded number with unbounded number.")

    def __ne__(self, y):
        """x != y"""
        if isinstance(y, bnum):
            return self.value != y.value
        else:
            raise TypeError("Can't compare bounded number with unbounded number.")

    def __ge__(self, y):
        """x >= y"""
        if isinstance(y, bnum):
            return self.value >= y.value
        else:
            raise TypeError("Can't compare bounded number with unbounded number.")

    def __gt__(self, y):
        """x > y"""
        if isinstance(y, bnum):
            return self.value > y.value
        else:
            raise TypeError("Can't compare bounded number with unbounded number.")

    def __le__(self, y):
        """x <= y"""
        if isinstance(y, bnum):
            return self.value <= y.value
        else:
            raise TypeError("Can't compare bounded number with unbounded number.")

    def __lt__(self, y):
        """x < y"""
        if isinstance(y, bnum):
            return self.value < y.value
        else:
            raise TypeError("Can't compare bounded number with unbounded number.")


b = bnum

b = bnum
