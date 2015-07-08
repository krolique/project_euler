Sub Array Sum
=============
The sub array problem go like this: suppose you are given an array of integers
(in our case they are all positive) and we want to determine if there is a 
consecutive sequence of integers that sum up to a particular sum.

Example::

    Given: [1, 3, 10, 20, 6, 50] and 14
    Answer: [1, 3, 10]

Seems simple enough, the algorithm for finding such a sum is trivial. Starting
from index zero keep adding values until you've reached the desired sum or
exceeded the desired sum. 

.. code:: python

    so_far = 0
    for idx, value in enumerate(array):
        so_far += value
        if so_far == desired_sum:
            return array[0:idx]
        if value > desired_sum:
            break
    return []


Well, this approach is great unless the consecutive sum of integers can be
found much later in the array.

Example::

    Given: [1, 3, 10, 20, 6, 50] and 36
    Answer: [10, 20, 6]

One may scratch their head a little and say "hey i can just iterate over
the initial array and then iterate over it again if the desired sum is not
found by going from index + 1". This approach will solve the problem...However
the run time of this would be polynomial and that's not so great when dealing
with large arrays. 

Suppose some one told you there's a way to implement this in linear time!


.. code:: python

    current_sum = array[0]
    start, end = 0, 0
    while end < len(array):
        if current_sum == desired_sum:
            # plus one because of zero index array
            return array[start:end+1]

        if current_sum <= desired_sum:
            end += 1
            if end < len(array):
                current_sum += array[end]
        else:
            current_sum -= array[start]
            start += 1
    return []

In a gist code above will adjust the *start* and *end* positions (or pointers)
in one of two interchangeable phases. If the sum is less than desired sum
*end* position will be moved and if the sum is greater than desired sum the
*start* position will be moved. When the *end* position is adjusted the each
element in the array at that index is added and when the *start* position is
adjusted the element at that index is removed. It would be best to run through
one example of how this algorithm works.


Initial parameters::

    Given: [1, 3, 10, 20, 6, 50] and 36

Loop 1::

    start   ↓ 
          [ 1, 3, 10, 20, 6, 50 ] current_sum = 0
    end     ↑

    start   ↓
          [ 1, 3, 10, 20, 6, 50 ] current_sum = 4
    end        ↑


Loop 2::

    start   ↓ 
          [ 1, 3, 10, 20, 6, 50 ] current_sum = 4
    end        ↑

    start   ↓
          [ 1, 3, 10, 20, 6, 50 ] current_sum = 14
    end           ↑

Loop 3::

    start   ↓ 
          [ 1, 3, 10, 20, 6, 50 ] current_sum = 14
    end           ↑

    start   ↓
          [ 1, 3, 10, 20, 6, 50 ] current_sum = 34
    end               ↑

Loop 4::

    start   ↓ 
          [ 1, 3, 10, 20, 6, 50 ] current_sum = 34
    end               ↑

    start   ↓
          [ 1, 3, 10, 20, 6, 50 ] current_sum = 40
    end                   ↑

During this loop the algorithm begins to move the *start* position forward
while the *end* position remains fixed. This is because we can't add any more
elements going forward, the current sum exceeds desired sum, so we have to
remove some of the earlier elements from the sum and reduce the size of our
window. The algorithm can also begin to move *end* position forward if the 
current sum is set to a value of less than desired sum.

Loop 5::

    start   ↓ 
          [ 1, 3, 10, 20, 6, 50 ] current_sum = 40
    end                   ↑

    start      ↓
          [ 1, 3, 10, 20, 6, 50 ] current_sum = 39
    end                   ↑


Loop 6::

    start      ↓ 
          [ 1, 3, 10, 20, 6, 50 ] current_sum = 39
    end                   ↑

    start         ↓
          [ 1, 3, 10, 20, 6, 50 ] current_sum = 36
    end                   ↑


Loop 7::

    start         ↓ 
          [ 1, 3, 10, 20, 6, 50 ] current_sum = 36
    end                   ↑

    return array[2:5]




