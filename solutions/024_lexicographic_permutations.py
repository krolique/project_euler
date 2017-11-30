# -*- coding: utf-8 -*-
"""

    Problem #24 - Lexicographic permutations
    ----------------------------------------

    A permutation is an ordered arrangement of objects. For example, 3124 is
    one possible permutation of the digits 1, 2, 3 and 4. If all of the
    permutations are listed numerically or alphabetically, we call it
    lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

        012   021   102   120   201   210

    What is the millionth lexicographic permutation of the digits
    0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

"""


from common import permutations


def problem():
    """ Attempt to solve the problem... """

    print 'problem #24'

    g = permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    p = [g.next() for x in xrange(10**6)]
    digits = ''.join(str(x) for x in p[-1])
    print 'the digits of the millionth perm are: %s' % digits


if __name__ == "__main__":

    problem()
