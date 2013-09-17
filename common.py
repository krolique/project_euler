# -*- coding: utf-8 -*-
"""

    Common
    ------

    Contains shared code

"""

from math import sqrt


# Let proper_divisors(n) be defined as the sum of proper divisors of n
# (numbers less than n which divide evenly into n).
proper_divisors = lambda x: [y for y in xrange(1, x) if x % y == 0]


def is_pandigital(value, digits='123456789'):
    """Return True if value is pandigital

    In mathematics, a pandigital number is an integer that in a given base has
    among its significant digits each digit used in the base at least once.
    For example:

        1023456789, 1023456798, 1023456879, 1023456897, 1023456978, 1023456987,
        1023457689

    :param value: number to run the test against
    :type value: int
    :param digits: the digit base to compare against
    :type digits: str
    :returns: bool
    """

    value = str(value)
    if len(value) is not len(digits):
        return False

    return 0 not in [c in value for c in digits]


def fib_generator():
    """ Creates a generator which will return the next Fibonacci number """

    # used by fib(), can get rather huge....
    fibs = {0: 0, 1: 1}

    def fib(n):
        """ Return n-th fibonacci number using a method developed
        by E. W. Dijkstra

        Copied from:
            http://en.literateprograms.org/Fibonacci_numbers_(Python)
        """

        if n in fibs:
            return fibs[n]
        if n % 2 == 0:
            fibs[n] = ((2 * fib((n / 2) - 1)) + fib(n / 2)) * fib(n / 2)
            return fibs[n]
        fibs[n] = (fib((n - 1) / 2) ** 2) + (fib((n+1) / 2) ** 2)
        return fibs[n]

    counter = 0
    while True:
        yield fib(counter), counter
        counter += 1


class Seive(object):
    """ Prime Number Seive """

    def __init__(self, upper_bound=0):
        """ """

        self.upper_bound = upper_bound
        self.seive = []
        self.eratosthenes_seive()

    def eratosthenes_seive(self):
        """ Returns prime numbers upto the number n using the sieve of
        eratosthenes method.

        """
        # Refinement: initially list odd numbers only, (3, 5, ..., n), and
        # count up using an increment of 2p in step 3, thus marking only odd
        # multiples of p greater than p itself. +1 to be inclusive
        self.seive = range(3, self.upper_bound+1, 2)
        # compute the size
        size = len(self.seive)
        i = 0
        while i <= sqrt(self.upper_bound):
            if self.seive[i]:
                for x in xrange(i + self.seive[i], size, self.seive[i]):
                    self.seive[x] = 0
            i += 1

    def __iter__(self):
        """ """

        if self.upper_bound > 1:
            yield 2

        for x in self.seive:
            if x:
                yield x


def permutations(seq, permutation=[]):
    """Returns a permutations generator

    Each `__next__` call will return the next permutation of a given sequence

    :param seq: sequence of characters to be permuted
    :type seq: list
    :param permutation: used to store carried over sequence characters during
                        recursion
    :type permutation: str
    :returns: generator
    """

    if not seq:
        yield permutation
    for i, v in enumerate(seq):
        for p in permutations(seq[0:i] + seq[i+1:], permutation + [seq[i]]):
            yield p
