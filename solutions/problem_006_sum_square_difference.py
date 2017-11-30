# -*- coding: utf-8 -*-
"""

    Problem #6 - Sum square difference
    ----------------------------------

    The sum of the squares of the first ten natural numbers is,

        1^2 + 2^2 + ... + 10^2 = 385

    The square of the sum of the first ten natural numbers is,

        (1 + 2 + ... + 10)^2 = 55^2 = 3025

    Hence the difference between the sum of the squares of the first ten
    natural numbers and the square of the sum is 3025 - 385 = 2640.

    Find the difference between the sum of the squares of the first one
    hundred natural numbers and the square of the sum.

"""


def problem_6():
    """ Attempt to solve the problem... """

    limit = 100
    square_sum = limit * ((limit + 1) * (2 * limit + 1)) / 6
    numbers_sum = (limit * (limit + 1) / 2) ** 2
    return numbers_sum - square_sum

if __name__ == "__main__":

    print 'problem #6'
    ANSWER = problem_6()
    print 'The difference between the sum of the square and square of the '\
          'sum of the one to one hundred natural numbers is: %d' % ANSWER
