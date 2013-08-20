# -*- coding: utf-8 -*-
"""

    Problem #15 - Lattice paths
    ---------------------------

    Starting in the top left corner of a 2×2 grid, and only being able to
    move to the right and down, there are exactly 6 routes to the bottom
    right corner.

    .. image:: _static/p_015.gif
        :align: center

    How many such routes are there through a 20×20 grid?

"""

from math import factorial

n = 20


def problem():
    """ Attempt to solve the problem... """

    print 'problem #15'

    # because we are restricted to left and down moves the problems comes down
    # to counting 2n (left and right) path choose n
    number_of_paths = factorial(2*n)/(factorial(n)**2)
    print 'the number of paths to the lattice is %s' % number_of_paths

if __name__ == "__main__":

    problem()
