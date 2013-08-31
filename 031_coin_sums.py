# -*- coding: utf-8 -*-
"""

    Problem #31 - Coin sums
    -----------------------

    In England the currency is made up of pound, £, and pence, p, and there
    are eight coins in general circulation:

        1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

    It is possible to make £2 in the following way:

        1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

    How many different ways can £2 be made using any number of coins?

"""


def problem():
    """ Attempt to solve the problem... """

    print 'problem #31'

    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    total = 200
    matrix = [0] * (total + 1)
    matrix[0] = 1

    for coin in coins:
      for j in range(coin, len(matrix)):
        matrix[j] += matrix[j - coin]

    print 'the number of combination to make %d is: %d' % (total, matrix[-1])

if __name__ == "__main__":

    problem()
