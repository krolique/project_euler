Permutations
============
The permutations problem is as follows::

    Given: "ABC"
    Answer: "ABC", "ACB", "BAC", "BCA", "CAB", "CBA"



.. code:: python

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