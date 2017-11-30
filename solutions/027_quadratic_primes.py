# -*- coding: utf-8 -*-
"""

    Problem #27 - Quadratic primes
    ------------------------------

    Euler discovered the remarkable quadratic formula:

        n² + n + 41

    It turns out that the formula will produce 40 primes for the consecutive
    values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41
    is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly
    divisible by 41.

    The incredible formula  n² − 79n + 1601 was discovered, which produces 80
    primes for the consecutive values n = 0 to 79. The product of the
    coefficients, −79 and 1601, is −126479.

    Considering quadratics of the form:

        n² + an + b, where |a| < 1000 and |b| < 1000

    where |n| is the modulus/absolute value of n e.g. |11| = 11 and |−4| = 4

    Find the product of the coefficients, a and b, for the quadratic
    expression that produces the maximum number of primes for consecutive
    values of n, starting with n = 0.

"""

from common import Seive

#: contains primes for fast lookup
primes = {x: 0 for x in Seive(1000000)}


def check(a, b):
    """ """

    p = []
    n = 0
    while True:
        v = n**2 + a*n + b
        if primes.get(v) is None:
            break
        p.append(v)
        n += 1
    return p


def problem():
    """ Attempt to solve the problem... """

    print 'problem #27'

    l = 0
    m_a = 0
    m_b = 0
    for a in xrange(-1000, 1000):
        for b in xrange(-1000, 1000):
            p = len(check(a, b))
            if p > l:
                l = p
                m_a = a
                m_b = b

    print 'the product of coefficients is %s' % (m_a * m_b)


if __name__ == "__main__":

    problem()
