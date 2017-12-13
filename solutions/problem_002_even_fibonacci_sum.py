# -*- coding: utf-8 -*-
"""

    Problem #2 - Even Fibonacci numbers
    -----------------------------------

    Each new term in the Fibonacci sequence is generated by adding the
    previous two terms. By starting with 1 and 2, the first 10 terms will be::

        1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

    By considering the terms in the Fibonacci sequence whose values do not
    exceed four million, find the sum of the even-valued terms.

"""

from common import fibonacci_generator


def problem_2():
    """ Attempt to solve the problem... """

    total = 0
    for value in fibonacci_generator():
        if value[1] >= 4000000:
            break
        if value[1] % 2 == 0:
            total += value[1]
    return total

if __name__ == "__main__":

    print 'problem #2'
    ANSWER = problem_2()
    print 'sum of even fibonacci numbers less than four million is: %d ' % \
          ANSWER