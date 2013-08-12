# -*- coding: utf-8 -*-
"""
    Problem #9
    ----------

    Special Pythagorean triplet

    A Pythagorean triplet is a set of three natural numbers, a < b < c,  for
    which:

        a^2 + b^2 = c^2

    For example:

        3^2 + 4^2 = 9 + 16 = 25 = 5^2.

    There exists exactly one Pythagorean triplet for which:

        a + b + c = 1000.

    Find the product abc.

"""

n = 1000


def pythagorean_tuple_generator(n):
    """ """

    for a in xrange(1, n):
        a_i = a**2
        for b in xrange(a+1, n):
            c = a_i + b**2
            c_1 = int(c**.5)
            if c_1**2 == c:
                yield a, b, c_1


def problem():
    """ Attempt to solve the problem... """

    print 'problem #9'

    for a, b, c in pythagorean_tuple_generator(n=n):
        _sum = a + b + c
        if _sum == n:
            product = a * b * c
            print 'Product of pythagorean tuple (%d, %d, %d) whose sum is '\
                  '%d <= %d is: %d' % (a, b, c, _sum, n, product)


if __name__ == "__main__":
    problem()
