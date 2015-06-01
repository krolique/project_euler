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

def problem():
    """ Attempt to solve the problem... """

    print 'problem #43'
    """ 
        |1|2|3|4|5|6|7|8|9|10
        |x|4|0|6|x|x|x|x|x|x|
        |x|x 0|6|3|x|x|x|x|x|
        |x|x|x|6|3|5|x|x|x|x|
        |x|x|x|x|3|5|7|x|x|x|
        |x|x|x|x|x|5|7|2|x|x|
        |x|x|x|x|x|x|7|2|8|x|
        |x|x|x|x|x|x|x|2|8|9|

    

    """

    pandigital_sum = 0
    subset_1 = [x for x in map(''.join, permutations('406')) if int(x) % 2 == 0]
    subset_2 = [x for x in map(''.join, permutations('063')) if int(x) % 3 == 0]
    subset_3 = [x for x in map(''.join, permutations('635')) if int(x) % 5 == 0]
    subset_4 = [x for x in map(''.join, permutations('357')) if int(x) % 7 == 0]
    subset_5 = [x for x in map(''.join, permutations('572')) if int(x) % 11 == 0]
    subset_6 = [x for x in map(''.join, permutations('728')) if int(x) % 13 == 0]
    subset_7 = [x for x in map(''.join, permutations('289')) if int(x) % 17 == 0]


    print subset_1
    print subset_2
    print subset_3
    print subset_4
    print subset_5
    print subset_6
    print subset_7
    m = ['1'] + subset_1 + subset_2 + subset_3 + subset_4 + subset_5 + subset_6 + subset_7
    print m
    for s1 in subset_1:
        print '1%s--2-7289' % s1


    print 'the sum of all 0-9 pandigital numbers is: %s' % pandigital_sum


if __name__ == "__main__":

    problem()
