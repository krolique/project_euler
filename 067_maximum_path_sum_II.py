# -*- coding: utf-8 -*-
"""

    Problem #67 - Maximum path sum II
    ---------------------------------

    By starting at the top of the triangle below and moving to adjacent numbers
    on the row below, the maximum total from top to bottom is 23.

                        3                       3
                       / \                     /
                      7   4                   7   4
                     / \ / \       =>          \
                    2   4   6               2   4   6
                   / \ / \ / \                   \
                  8   5   9   3           8   5   9   3

    That is, 3 + 7 + 4 + 9 = 23.

    Find the maximum total from top to bottom in 067_triangle.txt a 15K text 
    file containing a triangle with one-hundred rows.

    NOTE: This is a much more difficult version of Problem 18. It is not 
    possible to try every route to solve this problem, as there are 299
    altogether! If you could check one trillion (1012) routes every second it
    would take over twenty billion years to check them all. There is an 
    efficient algorithm to solve it. ;o)

"""

def problem():
    """ Attempt to solve the problem... """

    print 'problem #67'

    array = []
    with file('067_triangle.txt', 'r') as input_file:
        for line in input_file.read().splitlines():
            array.append(map(int, line.split()))

    while len(array) > 1:
        level_0, level_1 = array.pop(), array.pop()
        array.append(
            [max(level_0[i], level_0[i + 1]) + v for i, v in enumerate(level_1)]
        )

    print 'the maximum total from top to bottom of the triangle '\
            'is: %d' % array[0][0]


if __name__ == "__main__":

    problem()
