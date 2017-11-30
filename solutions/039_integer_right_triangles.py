# -*- coding: utf-8 -*-
"""

    Problem #39 - Integer right triangles
    -------------------------------------

    If p is the perimeter of a right angle triangle with integral length sides,
    {a,b,c}, there are exactly three solutions for p = 120.

        {20,48,52}, {24,45,51}, {30,40,50}

    For which value of p ≤ 1000, is the number of solutions maximised?

"""


def problem():
    """ Attempt to solve the problem... """

    print 'problem #39'

    max_p = 0
    max_len = 0
    for p in xrange(41, 1001):
        solutions = {}
        for a in xrange(1, p):
            for b in xrange(a, p):
                t = (a, b, int((a**2 + b**2)**0.5))
                if t[0]**2 + t[1]**2 == t[2]**2 and sum(t) == p:
                    solutions[str(sorted(t))] = t
        if len(solutions) > max_len:
            max_len = len(solutions)
            max_p = p

    print 'number of solutions if maximiesed at %s' % max_p


if __name__ == "__main__":

    problem()
