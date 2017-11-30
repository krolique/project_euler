# -*- coding: utf-8 -*-
"""

    Problem #43 - Sub-string divisibility
    -------------------------------------

    The number, 1406357289, is a 0 to 9 pandigital number because it is made up
    of each of the digits 0 to 9 in some order, but it also has a rather
    interesting sub-string divisibility property.

    Let d(1) be the 1st digit, d(2) be the 2nd digit, and so on. In this way,
    we note the following:

        d(2)d(3)d(4)  = 406 is divisible by 2
        d(3)d(4)d(5)  = 063 is divisible by 3
        d(4)d(5)d(6)  = 635 is divisible by 5
        d(5)d(6)d(7)  = 357 is divisible by 7
        d(6)d(7)d(8)  = 572 is divisible by 11
        d(7)d(8)d(9)  = 728 is divisible by 13
        d(8)d(9)d(10) = 289 is divisible by 17

    Find the sum of all 0 to 9 pandigital numbers with this property.

"""

from common import permutations


def problem_43():
    """ Attempt to solve the problem... """

    pandigital_sum = 0
    for item in map(''.join, permutations('1406357289')):
        if int(item[7:]) % 17 is not 0:
            continue
        if int(item[6:-1]) % 13 is not 0:
            continue
        if int(item[5:-2]) % 11 is not 0:
            continue
        if int(item[4:-3]) % 7 is not 0:
            continue
        if int(item[3:-4]) % 5 is not 0:
            continue
        if int(item[2:-5]) % 3 is not 0:
            continue
        if int(item[1:-6]) % 2 is not 0:
            continue
        pandigital_sum += int(item)
    return pandigital_sum


if __name__ == "__main__":

    print 'problem #43'
    ANSWER = problem_43()
    print 'the sum of all 0-9 pandigital numbers with sub string divisibility'\
           ' is: %d' % ANSWER
