# -*- coding: utf-8 -*-
"""

    Problem #48 - Self powers
    -------------------------

    The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

    Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

"""


def problem_48():
    """ Attempt to solve the problem... """

    return int(str(sum(x**x for x in range(1, 1001)))[-10:])

if __name__ == "__main__":

    print 'problem #48'
    ANSWER = problem_48()
    print 'The sum of last ten digits of the series is: %d' % ANSWER
