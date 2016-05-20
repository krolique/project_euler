Binary Search
=============


Procedure
---------
Given an array A of n elements with values or records A(0)...A(n−1) and target
value T, the following subroutine uses binary search to find the index of T 
in A.

Pseudo Code::

    Set L to 0 and R to n − 1.
    If L > R, the search terminates as unsuccessful. 
    Set m (the position of the middle element) to the floor of (L + R) / 2.
    If Am < T, set L to m + 1 and go to step 2.
    If Am > T, set R to m − 1 and go to step 2.
    If Am = T, the search is done; return m.



.. code:: python

    def binary_search(array, target):
        """ Performs Binary Search on an array of integers by finding the
        target number or returns -1 if the target number is not found """

        left, right = 0, len(array) - 1
        while True:
            if left > right:
                return -1
            idx = (left + right) // 2
            if array[idx] < target:
                min = idx + 1
            elif array[idx] > target:
                max = idx - 1
            else:
                return idx


