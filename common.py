# -*- coding: utf-8 -*-
"""

    Common
    ------

    Contains shared code

"""

from math import sqrt


def is_prime(number):
    """Returns true if a number is a prime number. This method uses the
    simplest and most naive method for checking primes.

    The Naive method
    The simplest primality test is as follows: Given an input number n, check
    whether any integer m from 2 to n − 1 evenly divides n (the division leaves
    no remainder). If n is divisible by any m then n is composite, otherwise it
    is prime.

    :param number: the number to check
    :type number: int
    :returns: bool
    """

    if number > 1:
        # easy first prime is 2
        if number == 2:
            return True
        # cannot be a prime number because it's a multiple of 2
        if number % 2 == 0:
            return False
        # If we take a closer look at the divisors, we will see that some of
        # them are redundant. The divisors just flip around and repeat.
        # Therefore we can further eliminate testing divisors greater than
        # sqrt(n).
        for divisor in xrange(2, int(number**(0.5))):
            if divisor % number == 0:
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

    number = 3
    while True:
        if is_prime(number):
            yield number
        number += 1


def is_pandigital(number, zero_fill=True):
    """Returns True or False if the number n is pandigital.

    This function returns True for formal pandigital numbers (defined below) as
    well as n-pandigital such as 4-pandigital => 1234. The formal definition is
    given below.

    A number is said to be pandigital if it contains each of the digits from 0
    to 9 (and whose leading digit must be nonzero). However, "zeroless"
    pandigital quantities contain the digits 1 through 9. Sometimes exclusivity
    is also required so that each digit is restricted to appear exactly once.
    For example, 6729/13458 is a (zeroless, restricted) pandigital fraction
    and 1023456789 is the smallest (zerofull) pandigital number.


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

    :param number: number to check if its pandigital or not
    :type number: int
    :param zero_fill: whether or not 0 should be included in determining if the
                      number is pandigital.
    :type zero_fill: bool
    :returns: bool -- indicating if the numer is pandigital or not
    """

    size = 10 if zero_fill else 9

    seen_numbers = {}
    while number > 0:
        remander = number % 10
        number = (number - remander) / 10
        if seen_numbers.get(remander) is not None:
            return False
        seen_numbers[remander] = 1

    return len(seen_numbers) == size


def simple_fibonacci_generator():
    """Create a simple fibonacci generator which does not use recursion

    The code was copied from `How to write the fibonacci sequence in python
    <http://stackoverflow.com/questions/494594/how-to-write-the-fibonacci-s
    equence-in-python>`_.
    """

    number_1, number_2 = 0, 1
    yield number_1
    yield number_2
    while True:
        number_1, number_2 = number_2, number_1 + number_2
        yield number_2


def fibonacci_generator():
    """ Creates a generator which will return the next Fibonacci number """

    # used by fib(), can get rather huge....
    fibs = {0: 0, 1: 1}

    def fib(number):
        """ Return n-th fibonacci number using a method developed
        by E. W. Dijkstra

        Copied from:
            http://en.literateprograms.org/Fibonacci_numbers_(Python)
        """

        if number in fibs:
            return fibs[number]
        if number % 2 == 0:
            fibs[number] = ((2 * fib((number / 2) - 1))
                            + fib(number / 2)) * fib(number / 2)
            return fibs[number]
        fibs[number] = (fib((number - 1) / 2) ** 2) + (fib((number+1) / 2)
                                                        ** 2)
        return fibs[number]

    counter = 0
    while True:
        yield counter, fib(counter)
        counter += 1


def simple_factorization(number):
    """ Returns a list of factors of the given number

    :param number: the number factor
    :type number: int
    :returns: list    
    """

    factors = []
    for i in xrange(2, int(sqrt(number))):
        while number % i == 0:
            factors.append(i)
            number = number / i
    if number > 1:
        factors.append(number)

    return factors


def recursive_gcd(a, b):
    """Returns the greatest common denominator by performing euclidean division

    This method uses "Euclidean algorithm"

    The Euclidean algorithm proceeds in a series of steps such that the output
    of each step is used as an input for the next one. Let k be an integer that
    counts the steps of the algorithm, starting with zero. Thus, the initial
    step corresponds to k = 0, the next step corresponds to k = 1, and so on.

    Each step begins with two nonnegative remainders r(k−1) and r(k−2). Since
    the algorithm ensures that the remainders decrease steadily with every
    step, rk−1 is less than its predecessor rk−2. The goal of the kth step is
    to find a quotient qk and remainder rk that satisfy the equation


        r(k−2) = q(k) * r(k−1) + r(k)


    and that have rk < rk−1. In other words, multiples of the smaller number
    r(k−1) are subtracted from the larger number r(k−2) until the remainder
    r(k) is smaller than r(k−1).

    In the initial step (k = 0), the remainders r−2 and r−1 equal a and b, the
    numbers for which the GCD is sought. In the next step (k = 1), the
    remainders equal b and the remainder r0 of the initial step, and so on.
    Thus, the algorithm can be written as a sequence of equations

        a =  q0 * b + r0
        b =  q1 * r0 + r1
        r0 = q2 * r1 + r2
        r1 = q3 * r2 + r3

    """

    if b == 0:
        return a
    return recursive_gcd(b, a % b)


def iterative_gcd(a, b):
    """Returns the greatest common denominator by performing euclidean division

    This method uses "Euclidean algorithm"

    The Euclidean algorithm proceeds in a series of steps such that the output
    of each step is used as an input for the next one. Let k be an integer that
    counts the steps of the algorithm, starting with zero. Thus, the initial
    step corresponds to k = 0, the next step corresponds to k = 1, and so on.

    Each step begins with two nonnegative remainders r(k−1) and r(k−2). Since
    the algorithm ensures that the remainders decrease steadily with every
    step, rk−1 is less than its predecessor rk−2. The goal of the kth step is
    to find a quotient qk and remainder rk that satisfy the equation


        r(k−2) = q(k) * r(k−1) + r(k)


    and that have rk < rk−1. In other words, multiples of the smaller number
    r(k−1) are subtracted from the larger number r(k−2) until the remainder
    r(k) is smaller than r(k−1).

    In the initial step (k = 0), the remainders r−2 and r−1 equal a and b, the
    numbers for which the GCD is sought. In the next step (k = 1), the
    remainders equal b and the remainder r0 of the initial step, and so on.
    Thus, the algorithm can be written as a sequence of equations

        a =  q0 * b + r0
        b =  q1 * r0 + r1
        r0 = q2 * r1 + r2
        r1 = q3 * r2 + r3

    """

    while b:
        temp = b
        b = a % b
        a = temp

    return a


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
