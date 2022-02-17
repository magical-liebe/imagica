"""Test for calc.py."""
from imagica import calc


def test_divide_internally_01() -> None:
    """Check divide_internally()."""
    p = calc.divide_internally((1, -2), (4, 10), (2, 1))
    assert p == (3, 6)


def test_divide_internally_02() -> None:
    """Check divide_internally()."""
    p = calc.divide_internally((16, 10), (4, -2), (1, 3))
    assert p == (13, 7)


def test_divide_externally_01() -> None:
    """Check divide_externally()."""
    p = calc.divide_externally((1, -2), (4, 10), (4, 1))
    assert p == (5, 14)


def test_divide_externally_02() -> None:
    """Check divide_externally()."""
    p = calc.divide_externally((16, 10), (4, -2), (1, 3))
    assert p == (22, 16)
