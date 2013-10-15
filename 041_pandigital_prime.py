# -*- coding: utf-8 -*-
"""

    Problem #41 - Pandigital prime
    ------------------------------

    We shall say that an n-digit number is pandigital if it makes use of all
    the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital
    and is also prime.

    What is the largest n-digit pandigital prime that exists?


"""

from common import is_pandigital, Seive

primes = [x for x in Seive(7999999)]


def problem():
    """ Attempt to solve the problem... """

    print 'problem #41'

    max_p = 0
    for prime in primes:
        if is_pandigital(prime):
            print prime
            if prime > max_p:
                max_p = prime
    print 'the largest n-digit pandigital number is %s' % max_p


if __name__ == "__main__":

    problem()
