# -*- coding: utf-8 -*-
"""

    Problem #28 - Number spiral diagonals
    -------------------------------------

    Starting with the number 1 and moving to the right in a clockwise direction
    a 5 by 5 spiral is formed as follows:

        21 22 23 24 25
        20  7  8  9 10
        19  6  1  2 11
        18  5  4  3 12
        17 16 15 14 13

    It can be verified that the sum of the numbers on the diagonals is 101.

    What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
    formed in the same way?

"""


def problem():
    """ Attempt to solve the problem... """

    print 'problem #28'

    depth = 1
    numbers = 0
    s = 0
    for x in xrange(1, 1001**2+1):
        numbers += 1
        if depth == 1 or numbers % (depth - 1) == 0:
            s += x
        if x / depth == depth:
            depth += 2
            numbers = 0
    print 'the sum of diagonal number is %s' % s


if __name__ == "__main__":

    problem()
