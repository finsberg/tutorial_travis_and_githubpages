import pytest
import mymodule

TOL = 1e-12


def test_add1():
    assert abs(mymodule.add(1, 1) - 2) < TOL


def test_add2():
    assert abs(mymodule.add(-1, -1) - -2) < TOL


def test_add3():
    assert abs(mymodule.add(-1, 1)) < TOL


def test_divide1():
    assert abs(mymodule.divide(2, 4) - 0.5) < TOL


def test_divide2():
    assert abs(mymodule.divide(-4, 2) - (-2)) < TOL


def test_divide3():
    with pytest.raises(ZeroDivisionError):
        mymodule.divide(1, 0)
