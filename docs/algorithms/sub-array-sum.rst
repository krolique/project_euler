Sub Array Sum
=============
The sub array problem go like this: suppose you are given an array of integers
(in our case they are all positive) and we want to determine if there is a 
consequtive sequence of integers that sum up to a particular sum.

Example::

    Given: [1, 3, 10, 20, 6, 50] and 14
    Answer: [1, 3, 10]

Seems simple enough, the algorithm for finding such a sum is trivial. Starting
from index zero keep adding values until you've reach the desired sum or
exceeded the desired sum. 

Python Code::

    so_far = 0
    for idx, value in enumerate(array):
        so_far += value
        if so_far == desired_sum:
            return array[0:idx]
        if value > desired_sum:
            break
    return []


Well, this approach is great unless the consequtive sum of integers can be
found much later in the array.

Example::

    Given: [1, 3, 10, 20, 6, 50] and 36
    Answer: [10, 20, 6]

One may scratch their head a little and say "hey i can just iterate over
the initial array and then iterate over it again if the desired sum is not
found by going from index + 1". This approach will solve the problem...However
the run time of this would be polynomial and that's not so great when dealing
with large arrays. 

Suppose some one told you theres a way to implement this in linear time!
Analogous to Kadane's algorithm



Lets examine the code::

    current_sum = array[0]
    start, end = 0, 0
    while end < len(array):
        if current_sum == desired_sum:
            return array[start:end+1]

        if current_sum <= desired_sum:
            end += 1
            if end < len(array):
                current_sum += array[end]
        else:
            current_sum -= array[start]
            start += 1
    # in the event nothing is found we should return an empty list as per
    # the function contract
    return []



    [1, 3, 4, 5, 6, 10]
        ^
