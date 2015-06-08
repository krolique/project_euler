# -*- coding: utf-8 -*-
"""

    Test answers
    ------------

    This module tests solution modules for correct answers

"""

from problem_001_multiples_of_3_and_5 import problem_1
from problem_002_even_fibonacci_sum import problem_2
from problem_003_largest_prime_factor import problem_3
from problem_004_largest_palindrone_product import problem_4
from problem_005_smallest_multiple import problem_5
from problem_006_sum_square_difference import problem_6


def test_answers():
    """Tests solution modules for correct answers"""

    assert problem_1() == 233168
    assert problem_2() == 4613732
    assert problem_3() == 6857
    assert problem_4() == 906609
    assert problem_5() == 232792560
    assert problem_6() == 25164150
