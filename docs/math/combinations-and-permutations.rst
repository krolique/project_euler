Combinations and Permutations
=============================
Combinations and permutations are the different ways we can count arrangements
of items. Combinations and permutations have special and distinct meanings that 
we should understand. 

The Distinction
---------------
We can find the distinction between Combinations and Permutations by reading
dictionary definitions for the two nouns::

    permutation |ˌpərmyo͝oˈtāSHən|
    noun
    1.  a way, especially one of several possible variations, in which a set or
        number of things can be ordered or arranged: his thoughts raced ahead to
        fifty different permutations of what he must do.

    2.  Mathematics the action of changing the arrangement, especially the
        linear order, of a set of items.

    combination |ˌkämbəˈnāSHən|
    noun
    1.  a joining or merging of different parts or qualities in which the
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

What distinguishes one noun from the other is the concern for the arrangement
of elements. If the arrangement of numbers 123 is the same as
321 when you are counting number of combinations otherwise its permutations.

What Are Permutations
---------------------
Permutations are unique arrangement of choices chosen from a predefined list
of items. By saying **unique** we are implying the arrangement of elements does
matters to us and we are concerned how things are arranged.

Permutations With Repetitions
-----------------------------
Permutations with repetitions are unique arrangements where a choice may appear
more one once. For instance::

    Given:  [a, b, c]

    Possible permutations with repetitions:     [a, a, a]
                                                [a, b, a]
                                                [c, c, a]

Let's derive a general rule for figuring out the number of permutations with
repetitions. Let's begin with the following example::

    Given:  [1, 2, 3, 4]
    Find: How many possible two-choice items are possible from the list?

We are tasked with finding how many ways can you arrange 2 things from this
list with repetitions. The possible two-choice arrangements would be::

    [1, 1] [1, 2] [1, 3] [1, 4]
    [2, 1] [2, 2] [2, 3] [2, 4]
    [3, 1] [3, 2] [3, 3] [3, 4]
    [4, 1] [4, 2] [4, 3] [4, 4]

Counting all the two-choice arrangements will reveal that there are 16
possible pairs. This approach is a bit lengthy, write out and then count
possible pairs and **"there must be a better way"** © Raymond Hettinger.
There is. 

The possible hint as to a better way of doing this may come from looking at
the matrix of possible choices and realizing you can get the total count, 
sixteen, by multiplying **4 by 4**. Further deduction from applying this
approach may reveal the following pattern::

    n * n

This formula can work with 1, 2, 3 or any number choices and the general rule 
for **r** number of choices from **n** number of things looks like this::

    n * n * n * ... = n ^ r

This is it, just multiply the number of choices by the number of times you are
asked to make a choice. This is the simplest case of figuring out unique item
arrangements. The next section is a bit more involved as we will have to figure
out how to count while excluding repetitions.

Permutations Without Repetitions
--------------------------------
Permutations without repetitions are unique arrangements where a choice may not
be used again. For instance::

    Given:  [a, b, c]

    Possible permutations without repetitions:     [a, b, c]
                                                   [c, b, a]
                                                   [b, c, a]

Continuing with our previous example where we have a list of 4 digits and want 
to pick 2 items but this time without repetitions.

Let's say we picked **1** then our options for the next number are limited to 
just: 2, 3 or 4. Because **1** cannot be selected again. Here is a list of
possible two-choice arrangements::

    [1, 2] [1, 3] [1, 4]
    
Thus given the first choice we can only pick from a set of 3 items for the next
choice or more precisely::

    (n - 1)
    
If we had to pick 3 items from the set the next number of choices would further
be reduced by the previous number of choices made::

    4 items to chose from
    ↓
    n * (n - 1) * (n - 2) ← 2 items to chose from
           ↑
           3 items to chose from

We again can generalize this pattern as a rule that looks like the this::

    n * (n - 1) * (n - 2) + ... + (n - r) [where r are the remaining choices]

Introspection into how each two-choice selection reduces the number of
remaining candidates will helps us understand how to construct the formula
for the general case. But before we get there we need to grasp a few more
concepts.

Let's workout another example to better understand what is happening to our
choices, because item-choice eliminations is what we are trying to establish.
Comparing permutations with and without repetitions should shed some light into
how we count possible permutations.

Let's by way of an example say we have 5 digits and we wanted to compute how
many permutations we can make from the whole set if we can pick only 3 items
with and without repetitions::

    5 * 4 * 3 * 2 * 1 = 120 [total choices with 5 items with repetitions]
    5 * 4 * 3         = 60  [total choices with 5 items but no repetitions]

The way we compute total choices without repetitions where we multiply each
number until exhaustion is actual a concept that you should either know or 
quickly ingest. More generally the way to express multiplying number one 
through n is generally know as this::

    5 * 4 * 3 * 2 * 1 = 5! [pronounced fakˈtôrēəl]

Factorials have a nice way of simplifying common mathematical operations
without "unfolding" the actual operations we are required to perform. For
instance we can compute from know values of factorials the following::

       5!       5 * 4 * 3 * 2 * 1    
    –––––––– = ––––––––––––––––––– = 5 * 4 = 20
     (5-2)!             3 * 2 * 1

Diverting our attention back from the factorial abstraction and focusing on the
actual application. The factorial representation can help us 
quickly calculate choices and in this case remove unwanted choices from
calculations. The break down of what we're doing is as follows::

    5 * 4 * 3 * 2 * 1                ← number of choices with repetitions
    –––––––––––––––––  = 5 * 4 = 20  ← remaining choices without repetitions
            3 * 2 * 1                ← number of choices excluded by 
                                       repetitions

Our formula should be able to calculate total number of permutations and remove
unwanted repetitive combinations. 

Which is what  have seen by means of representing
as a ration of factorial number can be written as total divided by exclusions.
The total portion looks like it can be written like this::

    (total number of choices)!

and the exclusions can be the choices we don't want to count (no repetitions)::

    (total number of choices - repetitions)!

Putting this all together our formula will look like this::

            n!
        –––––––––
         (n - r)!

And that's all there is to it, for permutations (ORDER MATTERS) without
repetitions we must remove repetitions in out total calculations.

What Are Combinations
---------------------
Combinations are arraignments of choices from a given list where the order doesn't
matter. For instance [1, 2, 3] and [3, 2, 1] are the same combination (if in 
fact we are dealing with combinations).

Combinations With Repetitions
-----------------------------
Combination with repetitions are arrangements of items where order does not
matter and we can select the same choice as many times as we would like to.
For instance::

    Given: [a, b, c, d, e]
    Possible combinations: [a, a, c]
                           [b, a, c]
                           [c, c, c]


With repetitions use the following formula::

     (n + r - 1)!
    –––––––––––––
    r! * (n - 1)!


Combinations Without Repetitions
--------------------------------
Combination without repetitions are arrangements of items where order does not
matter and we cannot repeat the same choice again. For instance::

    Given:  [A♤, K♤, Q♤, J♤, 10♤, 9♤, 8♤, 7♤, 6♤, 5♤, 4♤, 3♤, 2♤]

    Possible 5-card combinations without repetitions: [A♤,  K♤, Q♤, J♤, 10♤]
                                                      [10♤, 9♤, 8♤, 7♤,  6♤]
                                                      [6♤,  5♤, 4♤, 3♤,  2♤]

Observe that in combination of cards this hand [A♤,  K♤, Q♤, J♤, 10♤] should be
considered the same as this [10♤, A♤, K♤, Q♤, J♤] (order does not matter) and 
we cannot pick another card from the set twice. Choosing K♤ as first choice 
will prevent us from selecting this card again.

To find a general formula we must achieve the following::

    1.  Remove the number of items uniquely ordered.
        (i.e. the 5 pair hand [A♤,  K♤, Q♤, J♤, 10♤] and  [10♤, A♤, K♤, Q♤, J♤]
        should be only counted once)
    2.  Remove the number of duplicate choices within a given hand. (i.e.
        [A♤,  K♤, Q♤, J♤, J♤] and [A♤,  K♤, K♤, J♤, 10♤])


We should be able to use the permutations formula to achieve objective #1::

        n!          13!       13!
    ––––––––– = –––––––––– = ––––– = 154440
     (n - r)!    (13 - 5)!    8!

Objective #2 can be achieved by using the same permutations formula. Because 
we are trying to remove the number of ordered arrangements within a given hand
of 5 cards::

        n!          5!       5!
    ––––––––– = –––––––––– = –– = 120
     (n - r)!    (5 - 5)!    0!

Putting objective #1 and #2 together should yield a way to remove the unwanted
combinations. Let's state these two in a more precise form::

              P(n, r)        where P = # of permutations, C = # of combinations,
  C(n, r) = ––––––––––       n = # of items in the list and r = # of choices
              P(r, r)        from the list

Let's combine the two permutation equations into a single equation for
combination without repetitions::

                              n!        * Notice (r - r) = 0 and 0! = 1
                           ––––––––
              P(n, r)      (n - r)!        n!      (r - r)!       n!
  C(n, r) =  ––––––––– = –––––––––––– = –––––––– * –––––––– = –––––––––––
              P(r, r)       (r)!       (n - r)!      (r)!     r!(n - r)!
                          ––––––––
                          (r - r)!

This formula is also known as `Binomial Coefficient` and the number of
combinations given the set of 13 cards without repetitions is::

                P(13, 5)      13!         13!     13 * 12 * 11 * 10 * 9
    C(13, 5) = ––––––––– = –––––––––– = ––––––– = –––––––––––––––––––––– = 1287
                P(5, 5)    5!(13-5)!    5!* 8!    5 * 4 * 3 * 2 * 1


If repetitions are not allowed the number of combinations we can use the 
following formula::

         n!   
    –––––––––––––
    r! * (n - r)!
    