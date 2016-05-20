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
+--------------------------------+-----------+
| Characteristic                 |  Big-O    |
+--------------------------------+-----------+
| Worst case (Space Complexity‎)  |  O(1)     |
+--------------------------------+-----------+
| Best case                      |  O(1)     |
+--------------------------------+-----------+
| Average case                   |  O(log n) |
+--------------------------------+-----------+
| Worst case performance‎)        |  O(log n) |
+--------------------------------+-----------+


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

Initial parameters::

    Given: [1, 3, 10, 20, 23, 50] and 23

Loop 1::

    start
           L     M
           ↓     ↓
          [1, 3, 10, 20, 23, 50]
                         ↑
                         R
    end

We increment left (Step 4) by middle index + 1, which would be 3

Loop 2::

    start
                     L   M
                     ↓   ↓
          [1, 3, 10, 20, 23, 50]
                         ↑
                         R
    end

Because the value at index 4 is exactly the value we are looking for the
procedure returns index 4



