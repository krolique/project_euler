"""

    Problem 6
    =========

    Sum square difference

    The sum of the squares of the first ten natural numbers is,

        1^2 + 2^2 + ... + 10^2 = 385

    The square of the sum of the first ten natural numbers is,

        (1 + 2 + ... + 10)^2 = 55^2 = 3025

    Hence the difference between the sum of the squares of the first ten
    natural numbers and the square of the sum is 3025 - 385 = 2640.

    Find the difference between the sum of the squares of the first one
    hundred natural numbers and the square of the sum.

"""

#: bounds
n = 100


def problem():
    """ Attempt to solve the problem... """

    print 'problem #6'

    square_sum = n * ((n + 1) * (2*n + 1)) / 6
    numbers_sum = (n * (n + 1) / 2) ** 2
    difference = numbers_sum - square_sum
    print 'the differenc between sum of squares %d and the square of the sum'\
          ' %d is: %d' % (numbers_sum, square_sum, difference)

if __name__ == "__main__":
    problem()
