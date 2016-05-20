Binary Search
=============
In computer science, binary search, also known as half-interval search or
logarithmic search, is a search algorithm that finds the position of a
target value within a sorted array. It works by comparing the target
value to the middle element of the array; if they are unequal, the lower or
upper half of the array is eliminated depending on the result and the search is
repeated in the remaining subarray until it is successful.


Properties
----------

The following table describes the limiting behavior of an algorithm when the
argument tends towards a particular value or infinity

+---------+------------------+
| Case    |  Time Complexity |
+=========+==================+
| Best    |  O(1)            |
+---------+------------------+
| Average |  O(log n)        |
+---------+------------------+
| Worst   |  O(log n)        |
+---------+------------------+


Procedure
---------
Given an array A of n elements with values or records A(0)...A(n−1) and target
value T, the following subroutine uses binary search to find the index of T 
in A.

Pseudo Code::

    Step 1: Set L to 0 and R to n − 1.
    Step 2: If L > R, the search terminates as unsuccessful. 
    Step 3: Set m (the position of the middle element) to the floor of
            (L + R) / 2.
    Step 4: If A(m) < T, set L to m + 1 and go to step 2.
    Step 5: If A(m) > T, set R to m − 1 and go to step 2.
    Step 6: If A(m) = T, the search is done; return m.


Implementation
--------------

The following is a basic binary search function written in python

.. code:: python

    def binary_search(array, target):
        """ Performs Binary Search on an array of integers by finding the
        target number or return -1 if the target number is not found """

        left, right = 0, len(array) - 1
        while True:
            if left > right:
                return -1
            middle = (left + right) // 2
            if array[middle] < target:
                left = middle + 1
            elif array[middle] > target:
                right = middle - 1
            else:
                return middle

Lets run through a few examples and see how the algorithm actually works.

Example #1 where the target is in the right half of the array

Initial parameters::

    Given: [1, 3, 10, 20, 23, 50] and 23

We begin the procedure by setting the value for L to 0, R to 5 (length of the
array is 6 and 6 - 1 is 5) and M to 2 ( taking the floor of (0 + 5)/2 gives us
2) [Step 1] and begin our iteration over Steps 2 - 6. Since 0(L) < 2(R we 
continue to Step 3 and assign M the value of 2. Steps 1, 2 and 3 will be omitted
from all subsequent examples as the author finds copying this line laborious and
redundant.

Loop 1::

    start
           L(0)  M(2)
           ↓     ↓
          [1, 3, 10, 20, 23, 50]
                         ↑
                         R(5)
    end

Array value at A(2) is 10 and 10 < 23, we increment L [Step 4] by M + 1 and 
continue onto the next loop. Returning to Step 2 in algorithm execution.

Loop 2::

    start
                     L(3) M(4)
                     ↓    ↓
          [1, 3, 10, 20, 23, 50]
                          ↑
                          R(5)
    end

Array value at A(4) is 23 and 23 is the number we are looking for enabling us
to terminate the procedure by returning [Step 6] 4 as the index at which the
value exists.

Example #2 where the target at the end the array

Initial parameters::

    Given: [1, 3, 10, 20, 23, 50] and 50

Loop 1::

    start
           L(0)  M(2)
           ↓     ↓
          [1, 3, 10, 20, 23, 50]
                         ↑
                         R(5)
    end

Array value at A(2) is 10 and 10 < 50, we set the value of L [Step 4] to M + 1
and continue onto the next loop. Returning to Step 2 in algorithm execution.

Loop 2::

    start
                     L(3) M(4)
                     ↓    ↓
          [1, 3, 10, 20,  23, 50]
                          ↑
                          R(5)
    end

Array value at A(4) is 23 and 23 < 50, we set the value of L [Step 4] to M + 1
and continue onto the next loop. Returning to Step 2 in algorithm execution.

Loop 3::

    start
                             M(5)
                             L(5)
                             ↓
          [1, 3, 10, 20, 23, 50]
                          ↑
                          R(5)
    end

At this point Step 2 should be mentioned as the condition `<` will not
terminate the loop simply because 5 is not greater than 5. So we continue to the
next step. Array value at A(5) is 50 and 50 is the number we are looking for
enabling us to terminate the procedure by returning [Step 6] 5 as the index at
which the value exists.

Example #3 where the target is in the beginning the array

Initial parameters::

    Given: [1, 3, 10, 20, 23, 50] and 1

Loop 1::

    start
           L(0)  M(2)
           ↓     ↓
          [1, 3, 10, 20, 23, 50]
                         ↑
                         R(5)
    end

Array value at A(2) is 10 and 10 > 1, we set the value of R [Step 5] to M - 1
and continue onto the next loop. Returning to Step 2 in algorithm execution.

Loop 2::

    start
           M(0)
           L(0)
           ↓
          [1, 3, 10, 20, 23, 50]
              ↑
              R(1)
    end

The value for M is set to zero because::

    (L + R)   (0 + 1)    1
    ------- = ------- = ---, after taking the floor(0.5) we get 0
       2         2       2

Array value at A(0) is 1 and 1 is the number we are looking for enabling us to
terminate the procedure by returning [Step 6] 5 as the index at which the value
exists.

Example #4 where the target is in the left half the array

Initial parameters::

    Given: [1, 3, 10, 20, 23, 50] and 3

Loop 1::

    start
           L(0)  M(2)
           ↓     ↓
          [1, 3, 10, 20, 23, 50]
                         ↑
                         R(5)
    end

Array value at A(2) is 10 and 10 < 3, we set the value of R [Step 5] to M - 1
and continue onto the next loop. Returning to Step 2 in algorithm execution.

Loop 2::

    start
           M(0)
           L(0)
           ↓
          [1, 3, 10, 20, 23, 50]
              ↑
              R(1)
    end

Array value at A(0) is 1 and 1 > 3, we set the value of L [Step 4] to M + 1
and continue onto the next loop. Returning to Step 2 in algorithm execution.

Loop 3::

    start
              M(1)
              L(1)
              ↓
          [1, 3, 10, 20, 23, 50]
              ↑
              R(1)
    end

Array value at A(1) is 3 and 3 is the number we are looking for enabling us to
terminate the procedure by returning [Step 6] 5 as the index at which the value
exists.