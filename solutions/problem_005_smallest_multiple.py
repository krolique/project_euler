# -*- coding: utf-8 -*-
"""

    Problem #5 - Smallest multiple
    ------------------------------

    2520 is the smallest number that can be divided by each of the numbers
    from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of
    the numbers from 1 to 20?

"""

from common import lcm


def problem_5():
    """ Attempt to solve the problem... """

    answer = lcm(1, 2)
    # We can just continue to recalculate the lcm for each new number in the
    # list because: lcm(a,b,c) = lcm(a,lcm(b,c))
    for number in xrange(2, 20+1):
        print number
        answer = lcm(number, answer)

    return answer

if __name__ == "__main__":

    print 'problem #5'
    ANSWER = problem_5()
    print 'the smallest positive number that is evenly divisible by all of '\
          'the numbers from 1 to 20 is: %d' % ANSWER
