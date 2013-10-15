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


def is_prime(n):
    """Returns True or False if the number is a prime

    The Naive method
    The simplest primality test is as follows: Given an input number n, check
    whether any integer m from 2 to n − 1 evenly divides n (the division leaves
    no remainder). If n is divisible by any m then n is composite, otherwise it
    is prime.

    :param n: the number to check
    :type n: int
    :returns: bool
    """

    if n > 1:
        # easy first prime is 2
        if n == 2:
            return True
        # cannot be a prime number because it's a multiple of 2
        if n % 2 == 0:
            return False
        # If we take a closer look at the divisors, we will see that some of
        # them are redundant. The divisors just flip around and repeat.
        # Therefore we can further eliminate testing divisors greater than
        # sqrt(n).
        for i in xrange(2, int(n**(0.5))):
            if i % n == 0:
                return False
        return True
    return False


def prime_number_generator(start=None):
    """Creates a prime number generator, this generator uses the
    simplest and probably the most intensive method to generate prime numbers.

    However since it does not use a Sieve to precompute and store existing
    primes this method might be easier on the memory of the caller

    :param start: the number to start from
    :type start: int
    :returns: int
    """

    if not start:
        yield 2
        n = 3
    else:
        n = start
    while True:
        if is_prime(n):
            yield n
        n += 1


def is_pandigital(value):
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
    numbers = ''.join(str(x) for x in xrange(1, len(value)+1))
    return ''.join(sorted(value)) == numbers


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
