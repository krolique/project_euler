# -*- coding: utf-8 -*-
"""

    Problem #52 - Permuted multiples
    --------------------------------

    It can be seen that the number, 125874, and its double, 251748, contain
    exactly the same digits, but in a different order.

    Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
    contain the same digits.

"""


def problem_52():
    """ Attempt to solve the problem... """

    for number in xrange(1, 123456789):
        sorted_num = ''.join(sorted(str(number)))
        if len([value for value in xrange(2, 7)
                if ''.join(sorted(str((value * number)))) == sorted_num]) == 5:
            return number

if __name__ == "__main__":

    print 'problem #52'
    ANSWER = problem_52()
    print 'The smallest positive intgers x with this property is %s' % ANSWER
