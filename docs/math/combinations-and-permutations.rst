Combinations and Permutations
=============================
There are often enough time when you may wander how many possible combinations
(or permutations) can be made when you arrange things from a given set. Without
thinking we may use these two words interchangeably. However their meaning is
quite different depending upon what do you actually mean. The answer comes down
to a simple few questions.

    1. Does the order matter?

    2. Are repetitions allowed?

What's the Difference?
----------------------
Lets look at this noun in the dictionary::

    permutation |ˌpərmyo͝oˈtāSHən|
    noun
    1.  a way, especially one of several possible variations, in which a set or
        number of things can be ordered or arranged: his thoughts raced ahead to
        fifty different permutations of what he must do.

    2.  Mathematics the action of changing the arrangement, especially the
        linear order, of a set of items.

and now lets look at the other noun definition::

    combination |ˌkämbəˈnāSHən|
    noun

    1.  
        - a joining or merging of different parts or qualities in which the
        component elements are individually distinct: a combination of
        blackberries, raspberries, and rhubarb | this color combination is
        stunningly effective.
        
        - the process of combining different parts or qualities or the state of
        being combined: these four factors work together in combination.
        
        - an arrangement of elements: the canvases may be arranged in any
        number of combinations.
        
        - (in various sports and games) a coordinated and effective sequence of
        moves: a good uppercut/hook combination.

        - [ as modifier ] uniting different uses, functions, or ingredients: a
        combination garment bag and backpack.

        - Chemistry the joining of substances in a compound with new properties.

    2.  a sequence of numbers or letters used to open a combination lock:
        [ as modifier ] : a combination briefcase.

    3.  Mathematics a selection of a given number of elements from a larger
        number without regard to their arrangement.


The `regard` for order becomes apparent from the definition of `combinations`
and so the distinctions boils down to the order of elements.

if 123 is the same as 321 to you then its combinations you are referring to but
if not, such as a password of 123 is not the same as 321, then its
permutations.


Permutations
------------
Order matters, order matters, order matters (in that order!)


Repetitions
~~~~~~~~~~~
When repetitions are allowed, we can pick the number 7 from a set of digits in
each of our choices, we can use the following formula to figure out the number
of permutations with repetitions::

    n * n * n + ... + n = n ^ x

No Repetitions
~~~~~~~~~~~~~~
If repetitions of elements in each permutation are not allowed we are faced with
a reduces set on items to chose from at each iteration::

    n * (n - 1) * (n - 2) + ... + (n - r)

This can be written as a formula in the following fashion::

            n!
        ---------
         (n - r)!

Combinations
------------
We don't care about positions of each choice! We don't care about the position
of each choice! (like totally!)

Repetitions
~~~~~~~~~~~

     (n + r - 1)!
    --------------
    r! * (n - 1)!


No Repetitions
~~~~~~~~~~~~~~
If repetitions are not allowed the number of combinations is broken down as
follows::

             n!
        -------------
        r! * (n - r)!

Also known as `Binomial Coefficient`, and this equation is just like
permutations with the added effect of removing the number of time each
combination could be in order


    