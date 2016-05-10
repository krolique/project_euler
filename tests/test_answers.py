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
from problem_007_10001st_prime import problem_7
from problem_043_sub_string_divisibility import problem_43
from problem_044_pentagon_numbers import problem_44
from problem_046_goldbachs_other_conjecture import problem_46
from problem_047_distinct_primes_factors import problem_47
from problem_048_self_powers import problem_48
from problem_050_consecutive_prime_sum import problem_50
from problem_052_permuted_multiples import problem_52


def test_answers():
    """Tests solution modules for correct answers"""

    assert problem_1() == 233168
    assert problem_2() == 4613732
    assert problem_3() == 6857
    assert problem_4() == 906609
    assert problem_5() == 232792560
    assert problem_6() == 25164150
    assert problem_7() == 104743
    assert problem_43() == 16695334890
    assert problem_44() == 5482660
    assert problem_46() == 5777
    assert problem_47() == 134043
    assert problem_48() == 9110846700
    assert problem_50() == 997651
    assert problem_52() == 142857
