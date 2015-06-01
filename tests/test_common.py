# -*- coding: utf-8 -*-
"""

    Common module tests
    -------------------

    Contains unit tests for the common module

"""

from common import (is_pandigital, simple_fibonacci_generator,
                    fibonacci_generator, simple_factorization, recursive_gcd,
                    iterative_gcd)

FIBONACCI_NUMBERS = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377,
                     610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657,
                     46368, 75025, 121393, 196418, 317811, 514229, 832040,
                     1346269, 2178309, 3524578, 5702887, 9227465, 14930352,
                     24157817, 39088169]

#: list of numbers copied from http://oeis.org/A050278
ZEROFILL_PANDIGITAL_NUMBERS = [1023456789, 1023456798, 1023456879, 1023456897,
                               1023456978, 1023456987, 1023457689, 1023457698,
                               1023457869, 1023457896, 1023457968, 1023457986,
                               1023458679, 1023458697, 1023458769, 1023458796,
                               1023458967, 1023458976, 1023459678, 1023459687,
                               1023459768]

NONZERO_PANDIGITAL_NUMBERS = [123456789, 123456798, 123456879, 123456897,
                              123456978, 123456987, 123457689, 123457698,
                              123457869, 123457896, 123457968, 123457986,
                              123458679, 123458697, 123458769, 123458796,
                              123458967, 123458976, 123459678, 123459687,
                              123459768]

def test_iterative_gcd():
    """Tests the iterative gcd method """

    assert iterative_gcd(4230, 10392) == 6
    assert iterative_gcd(4, 20) == 4
    assert iterative_gcd(0, 0) == 0
    assert iterative_gcd(0, 1) == 1


def test_recursive_gcd():
    """Tests the recursive gcd method """

    assert recursive_gcd(4230, 10392) == 6
    assert recursive_gcd(4, 20) == 4
    assert recursive_gcd(0, 0) == 0
    assert recursive_gcd(0, 1) == 1


def test_simple_factorization():
    """Tests simple factorization method """

    assert simple_factorization(20) == [2, 2, 5]
    assert simple_factorization(201929) == [7, 7, 13, 317]
    assert simple_factorization(0) == []
    assert simple_factorization(1) == []
    assert simple_factorization(12) == [2, 2, 3]
    assert simple_factorization(17) == [17]



def test_simple_finonacci_gen_output():
    """Tests simple fibanacci generator output """

    for index, number in enumerate(simple_fibonacci_generator()):
        #: since the generator is infinite, we'd like to terminate at some
        #: point
        if index >= len(FIBONACCI_NUMBERS):
            break
        assert number == FIBONACCI_NUMBERS[index]


def test_fib_generator():
    """Tests fib generator output """

    for index, number in fibonacci_generator():
        #: since the generator is infinite, we'd like to terminate at some
        #: point
        if index >= len(FIBONACCI_NUMBERS):
            break
        assert number == FIBONACCI_NUMBERS[index]


def test_is_pandigital_non_zerofill_valid():
    """Tests valid non zerofill pandigital numbers"""

    for number in ZEROFILL_PANDIGITAL_NUMBERS:
        assert is_pandigital(number, True) is True


def test_is_pandigital_zerofill_valid():
    """Tests valid zerofill pandigital numbers """

    for number in NONZERO_PANDIGITAL_NUMBERS:
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
