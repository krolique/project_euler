# -*- coding: utf-8 -*-
"""

    Common
    ------

    Contains shared code

"""

from math import sqrt, fabs


def is_prime(number):
    """Returns true if a number is a prime number. This method uses the
    simplest and most naive method for checking primes.

    The Naive method
    The simplest primality test is as follows: Given an input number n, check
    whether any integer m from 2 to n − 1 evenly divides n (the division leaves
    no remainder). If n is divisible by any m then n is composite, otherwise it
    is prime.

    :param number: the number to check
    :type number: int
    :returns: bool
    """

    if number > 1:
        # easy first prime is 2
        if number == 2:
            return True
        # cannot be a prime number because it's a multiple of 2
        if number % 2 == 0:
            return False

        #: The optimization in checking divisors less than sqrt(n) can be
        #: explained with proof by contradiction. If n is not a prime then
        #: there exists two numbers such that n = a*b where either a or b must
        #: be less than or equal to the sqrt(n). If both were to be greater
        #: than the square root of n then the product of a*b would be greater
        #: than n. If we can prove that there is such a or b that is less that
        #: sqrt(n) then we can prove n is not a prime. The search for a number
        #: would add another factor into factorization of n and disprove the
        #: primality of n. Another proof of this optimization can be derived
        #: from observing that some of the divisors after the sqrt(n) boundry
        #: are really multiples of earlier divisors. So we can just skip
        #: testing those.
        for divisor in xrange(2, int(number**(0.5))):
            if divisor % number == 0:
                return False
        return True
    return False


def prime_number_generator(start=None):
    """Creates a prime number generator, this generator uses the
    simplest and probably the most intensive method to generate prime numbers.

    However since it does not use a Sieve to precompute and store existing
    primes this method might be easier on the memory of the caller

    :param start: the number to start from
    :type start: int
    :returns: int
    """

    if not start:
        yield 2

    number = 3
    while True:
        if is_prime(number):
            yield number
        number += 1


def is_pandigital(number, zero_fill=True):
    """Returns True or False if the number n is pandigital.

    This function returns True for formal pandigital numbers (defined below) as
    well as n-pandigital such as 4-pandigital => 1234. The formal definition is
    given below.

    A number is said to be pandigital if it contains each of the digits from 0
    to 9 (and whose leading digit must be nonzero). However, "zeroless"
    pandigital quantities contain the digits 1 through 9. Sometimes exclusivity
    is also required so that each digit is restricted to appear exactly once.
    For example, 6729/13458 is a (zeroless, restricted) pandigital fraction
    and 1023456789 is the smallest (zerofull) pandigital number.


    ======== ====================== =======================
     Base     Smallest pandigital    Values in base 10
    ======== ====================== =======================
     2        10                     2
     3        102                    11
     4        1023                   75
     10       1023456789             1023456789
     16       1023456789ABCDEF       1162849439785405935
     Roman    MCDXLIV                1444
    ======== ====================== =======================

    :param number: number to check if its pandigital or not
    :type number: int
    :param zero_fill: whether or not 0 should be included in determining if the
                      number is pandigital.
    :type zero_fill: bool
    :returns: bool -- indicating if the numer is pandigital or not
    """

    size = 10 if zero_fill else 9

    seen_numbers = {}
    while number > 0:
        remander = number % 10
        number = (number - remander) / 10
        if seen_numbers.get(remander) is not None:
            return False
        seen_numbers[remander] = 1

    return len(seen_numbers) == size


def simple_fibonacci_generator():
    """Create a simple fibonacci generator which does not use recursion

    The code was copied from `How to write the fibonacci sequence in python
    <http://stackoverflow.com/questions/494594/how-to-write-the-fibonacci-s
    equence-in-python>`_.
    """

    number_1, number_2 = 0, 1
    yield number_1
    yield number_2
    while True:
        number_1, number_2 = number_2, number_1 + number_2
        yield number_2


def fibonacci_generator():
    """ Creates a generator which will return the next Fibonacci number """

    # used by fib(), can get rather huge....
    fibs = {0: 0, 1: 1}

    def fib(number):
        """ Return n-th fibonacci number using a method developed
        by E. W. Dijkstra

        Copied from:
            http://en.literateprograms.org/Fibonacci_numbers_(Python)
        """

        if number in fibs:
            return fibs[number]
        if number % 2 == 0:
            fibs[number] = ((2 * fib((number / 2) - 1))
                            + fib(number / 2)) * fib(number / 2)
            return fibs[number]
        fibs[number] = (fib((number - 1) / 2) ** 2) + (fib((number+1) / 2)
                                                        ** 2)
        return fibs[number]

    counter = 0
    while True:
        yield counter, fib(counter)
        counter += 1


def simple_factorization(number):
    """ Returns a list of factors of the given number

    :param number: the number factor
    :type number: int
    :returns: list    
    """

    factors = []
    for i in xrange(2, int(sqrt(number))):
        while number % i == 0:
            factors.append(i)
            number = number / i
    if number > 1:
        factors.append(number)

    return factors


def recursive_gcd(a, b):
    """Returns the greatest common denominator by performing euclidean division

    This method uses "Euclidean algorithm"

    The Euclidean algorithm proceeds in a series of steps such that the output
    of each step is used as an input for the next one. Let k be an integer that
    counts the steps of the algorithm, starting with zero. Thus, the initial
    step corresponds to k = 0, the next step corresponds to k = 1, and so on.

    Each step begins with two nonnegative remainders r(k−1) and r(k−2). Since
    the algorithm ensures that the remainders decrease steadily with every
    step, rk−1 is less than its predecessor rk−2. The goal of the kth step is
    to find a quotient qk and remainder rk that satisfy the equation


        r(k−2) = q(k) * r(k−1) + r(k)


    and that have rk < rk−1. In other words, multiples of the smaller number
    r(k−1) are subtracted from the larger number r(k−2) until the remainder
    r(k) is smaller than r(k−1).

    In the initial step (k = 0), the remainders r−2 and r−1 equal a and b, the
    numbers for which the GCD is sought. In the next step (k = 1), the
    remainders equal b and the remainder r0 of the initial step, and so on.
    Thus, the algorithm can be written as a sequence of equations

        a =  q0 * b + r0
        b =  q1 * r0 + r1
        r0 = q2 * r1 + r2
        r1 = q3 * r2 + r3

    """

    if b == 0:
        return a
    return recursive_gcd(b, a % b)


def iterative_gcd(a, b):
    """Returns the greatest common denominator by performing euclidean division

    This method uses "Euclidean algorithm"

    The Euclidean algorithm proceeds in a series of steps such that the output
    of each step is used as an input for the next one. Let k be an integer that
    counts the steps of the algorithm, starting with zero. Thus, the initial
    step corresponds to k = 0, the next step corresponds to k = 1, and so on.

    Each step begins with two nonnegative remainders r(k−1) and r(k−2). Since
    the algorithm ensures that the remainders decrease steadily with every
    step, rk−1 is less than its predecessor rk−2. The goal of the kth step is
    to find a quotient qk and remainder rk that satisfy the equation


        r(k−2) = q(k) * r(k−1) + r(k)


    and that have rk < rk−1. In other words, multiples of the smaller number
    r(k−1) are subtracted from the larger number r(k−2) until the remainder
    r(k) is smaller than r(k−1).

    In the initial step (k = 0), the remainders r−2 and r−1 equal a and b, the
    numbers for which the GCD is sought. In the next step (k = 1), the
    remainders equal b and the remainder r0 of the initial step, and so on.
    Thus, the algorithm can be written as a sequence of equations

        a =  q0 * b + r0
        b =  q1 * r0 + r1
        r0 = q2 * r1 + r2
        r1 = q3 * r2 + r3

    """

    while b:
        temp = b
        b = a % b
        a = temp

    return a


def lcm(a, b):
    """ Returns the lowest common multiple of a and b

    A multiple of a number is the product of that number and an integer.
    For example, 10 is a multiple of 5 because 5 * 2 = 10, so 10 is
    divisible by 5 and 2. Because 10 is the smallest positive integer that is
    divisible by both 5 and 2, it is the least common multiple of 5 and 2.

    By the same principle, 10 is the least common multiple of -5 and 2 as well.
    The following formula reduces the problem of computing the least common
    multiple to the problem of computing the greatest common divisor (GCD):

        lcm(a, b) = abs(a*b)/gcd(a,b)

    """

    return fabs(a * b) / iterative_gcd(a, b)

def seive_generator(upper_bound):
    """The prime number seive

    A prime number is a natural number that has exactly two distinct natural
    number divisors: 1 and itself.

    To find all the prime numbers less than or equal to a given integer n by 
    Eratosthenes' method:

        1. Create a list of consecutive integers from 2 through n: 
                (2, 3, 4, ..., n).

        2. Initially, let p equal 2, the first prime number.

        3. Starting from p, enumerate its multiples by counting to n in
           increments of p, and mark them in the list (these will be 2p, 3p,
            4p, ... ; the p itself should not be marked).

        4. Find the first number greater than p in the list that is not marked.
           If there was no such number, stop. Otherwise, let p now equal this
           new number (which is the next prime), and repeat from step 3.

    When the algorithm terminates, the numbers remaining not marked in the list
    are all the primes below n.

    The main idea here is that every value for p is prime, because we have
    already marked all the multiples of the numbers less than p. Note that
    some of the numbers being marked may have already been marked earlier
    (e.g., 15 will be marked both for 3 and 5).

    As a refinement, it is sufficient to mark the numbers in step 3 starting
    from p2, as all the smaller multiples of p will have already been marked
    at that point. This means that the algorithm is allowed to terminate in
    step 4 when p2 is greater than n.

    Another refinement is to initially list odd numbers only, (3, 5, ..., n),
    and count in increments of 2p in step 3, thus marking only odd multiples
    of p. This actually appears in the original algorithm.[1] This can be
    generalized with wheel factorization, forming the initial list only from
    numbers coprime with the first few primes and not just from odds (i.e.,
    numbers coprime with 2), and counting in the correspondingly adjusted
    increments so that only such multiples of p are generated that are coprime
    with those small primes, in the first place.

    The sieving can also be done in consecutive segments, both to reduce
    memory requirements and to enhance performance due to CPU cache usage.

    See more:
        http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

    """

    #: first prime number is two
    yield 2

    if upper_bound < 3:
        return

    lmtbf = (upper_bound - 3) // 2
    buf = [True] * (lmtbf + 1)
    for i in range((int(upper_bound ** 0.5) - 3) // 2 + 1):
        if buf[i]:  
            p = i + i + 3
            #: As a refinement, it is sufficient to mark the numbers in step 3
            #: starting from p2, as all the smaller multiples of p will have
            #: already been marked at that point. This means that the algorithm
            #: is allowed to terminate in step 4 when p2 is greater than n.[1]
            s = p * (i + 1) + i
            #: optimized to use slice operations for composite number culling
            #: to avoid extra work by the interpreter:
            buf[s::p] = [False] * ((lmtbf - s) // p + 1)
    
    for i in range(lmtbf + 1):
        if buf[i]:
            yield (i + i + 3)


def permutations(seq, permutation=[]):
    """Returns a permutations generator

    Each `__next__` call will return the next permutation of a given sequence

    :param seq: sequence of characters to be permuted
    :type seq: list
    :param permutation: used to store carried over sequence characters during
                        recursion
    :type permutation: str
    :returns: generator
    """

    if not seq:
        yield permutation
    for i, v in enumerate(seq):
        for p in permutations(seq[0:i] + seq[i+1:], permutation + [seq[i]]):
            yield p
