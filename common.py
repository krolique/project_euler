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
    """Return True or False if the number is a prime

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


def is_pandigital(n, zero_fill=True, base=10):
    """Returns True or False if the number n is pandigital.

    This function returns True for formal pandigital numbers (defined below) as
    well as n-pandigital such as 4-pandigital => 1234. The formal definition is
    given below.

    A number is said to be pandigital if it contains each of the digits from 0
    to 9 (and whose leading digit must be nonzero). However, "zeroless"
    pandigital quantities contain the digits 1 through 9. Sometimes exclusivity
    is also required so that each digit is restricted to appear exactly once.
    For example, 6729/13458 is a (zeroless, restricted) pandigital fraction and
    1023456789 is the smallest (zerofull) pandigital number.


    ======== ====================== =======================
     Base     Smallest pandigital    Values in base 10
    ======== ====================== =======================
     2        10                     2
     3        102                    11
     4        1023                   75
     10       1023456789             1023456789
     16       1023456789ABCDEF       1162849439785405935
     Roman    MCDXLIV                1444
    ======== ====================== =======================

    :param n: number to check if its pandigital or not
    :type n: int
    :param zero_fill: whether or not 0 should be included in determining if the
                      number is pandigital.
    :type zero_fill: bool
    :param base: In mathematical numeral systems, the radix or base is the
                 number of unique digits, including zero, that a positional
                 numeral system uses to represent numbers. For example, for the
                 decimal system (the most common system in use today) the radix
                 is ten, because it uses the ten digits from 0 through 9.
    :type base: int
    :returns: bool -- indicating if the numer is pandigital or not
    """

    if base > 10:
        raise Exception('This method is not designed to handle bases higher '
                        'than 10')

    check_list = list(xrange(0, base))



def simple_fibonacci_generator():
    """Create a simple fibonacci generator which does not use recursion

    The code was copied from `How to write the fibonacci sequence in python
    <http://stackoverflow.com/questions/494594/how-to-write-the-fibonacci-s
    equence-in-python>`_.
    """

    a, b = 0, 1
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b

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
