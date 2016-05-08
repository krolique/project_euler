Permutations
============
The permutations problem is as follows::

    Given:  'ABC'
    Answer: ['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA'



.. code:: python

    def permutations(seq, permutation=[]):
        if not seq:
            yield permutation
        for i, v in enumerate(seq):
            for p in permutations(seq[0:i] + seq[i+1:], permutation + [seq[i]]):
                yield p


step 1::

    ['a', 'b', 'c']

    ['a'] ['b', 'c']





