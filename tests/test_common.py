# -*- coding: utf-8 -*-
"""

    Common module tests
    -------------------

    Contains unit tests for the common module

"""

from common import is_pandigital


def test_is_pandigital_non_zerofill_valid():
    """Tests valid non zerofill pandigital numbers"""

    #: list of numbers copied from http://oeis.org/A050278
    panditial_numbers = [1023456789, 1023456798, 1023456879, 1023456897,
                         1023456978, 1023456987, 1023457689, 1023457698,
                         1023457869, 1023457896,
                         1023457968, 1023457986, 1023458679, 1023458697,
                         1023458769, 1023458796, 1023458967, 1023458976,
                         1023459678, 1023459687, 1023459768]

    for number in panditial_numbers:
        assert is_pandigital(number, True) is True


def test_is_pandigital_zerofill_valid():
    """Tests valid zerofill pandigital numbers """

    panditial_numbers = [123456789, 123456798, 123456879, 123456897,
                         123456978, 123456987, 123457689, 123457698,
                         123457869, 123457896,
                         123457968, 123457986, 123458679, 123458697,
                         123458769, 123458796, 123458967, 123458976,
                         123459678, 123459687, 123459768]

    for number in panditial_numbers:
        assert is_pandigital(number, False) is True


def test_is_pandigital_invalid():
    """Tests the is_pandigital function with invalid numbers"""

    #: testing for numbers outside of the 9-10 digits range
    assert is_pandigital(123, True) is False
    assert is_pandigital(123, False) is False
    assert is_pandigital(123456789010, False) is False
    #: testing for zero
    assert is_pandigital(0, True) is False
    #: testing for repreating digits
    assert is_pandigital(1234567899, True) is False


def test_is_pandigital_none_value():
    """Tests the is_pandigital function with None value """

    assert is_pandigital(None) is False
