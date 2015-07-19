Combinations and Permutations
=============================
There are often enough times when you may wander how many possible combinations
(or permutations [the distinction will be made clearer a bit later]) can be made
when you arrange things in a given list. Without thinking we may use
combinations and permutations as nouns interchangeably. However their meaning 
is quite different depending upon what you actually mean and the distinction
between the two is made by answering the following questions:

1. Does the order matter?
2. Are repetitions allowed?

The Distinction
---------------
Lets look at the nouns in the dictionary::

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


Disregard for order becomes apparent from the definition of `combinations`.
The sub definition #3 in which we are told in mathematics the order of items
in a combination DOES NOT MATTER. Ta-Da!

If 123 is the same as 321 then we are going to count combinations. When
123 is not the same as 321 (such as a computer password) then we are going to
count permutations. 

Permutations
------------
Repeat after me: Order matters, order matters, order matters (in that order!).
Once this little bit of news settles or galvanizes we can then narrow down
counting ordered things with and without repetitions (without repetitions we
can only see an item from our ordered list [also called a set] only once) as
you will see in a little bit is slightly different from one another.


Repetitions
-----------
Say we are asked to find how many possible permutations are there given that
we have a list of items (apple, banana, pear would be one such list) and we want
to pick anywhere between one to all the items from this list?

Let's run through one example. If you had to deal with just a simple list of 
4 digits::

    [1, 2, 3, 4]

and you wanted to pick only 2 things from it while not worrying if you see any
number twice. Then the possible list of tuples for this could be::

    [1, 1] [1, 2] [1, 3] [1, 4]
    [2, 1] [2, 2] [2, 3] [2, 4]
    [3, 1] [3, 2] [3, 3] [3, 4]
    [4, 1] [4, 2] [4, 3] [4, 4]

If you did the all work and counted the possible tuples you should have reach a
conclusion that there are 16 possible combinations given the two premises.
Great! You can count and definitely arrange things. However once the number of
items in the list increases and perhaps the number of choices as well you may
find it laborious to count and arrange so many things. In fact you may even
abandon the idea and pursue a more leisurely activity. Unless! Unless there is
a theory of generalitivity (I know it's not a word, and I know it's terrible
to make inside jokes at the expense of time-space continuum)!

Let's begin this process by looking at how we can just reason about items
in the list and their arrangments. One initial derivation from the previous
example can be made: we have a 4 by 4 grid out of which we can form 16
possible choices. Which can state mathematically as follows::

    n * n

Each **n** for each pick from the set. Knowing this we can derive a general
rule that looks like this::

    n * n * n + ... + n = n ^ x

No Repetitions
--------------
Continuing with our previous example where we have a set of 4 digits and want 
to pick 2 items but without repetions (if first chocie was 2 then the next
choice cannot be 2)

Let's say we picked **1** then our options for the next number are 2, 3 or 4
or the following tuples::

    [1, 2] [1, 3] [1, 4]
    
Thus given the first choice we can only pick from a set of 3 items for the next
choice or more precisely stated::

    (n - 1)
    
If we had to pick 3 items from the set the next number of choices would further
be reduced by the previous number of choices made::

    4 items to chose from
    ↓
    n * (n - 1) * (n - 2) ← 2 items to chose from
           ↑
           3 items to chose from

We again can generalize this pattern as a rule that looks like the following::

    n * (n - 1) * (n - 2) + ... + (n - r) [where r is the remaining choices]

Let's work an example, say we have 5 digits and we wanted to compute how
many permutations we can make from the whole set and if we chose only 3::

    5 * 4 * 3 * 2 * 1 = 120 [choosing 5 items without repetitions]
    5 * 4 * 3         = 60  [choosing 3 out of 5 total items without repetitions]

This observation may or many not lead you to an even better formula for 
figuring out permutations without repetitions. First observe that::

    5 * 4 * 3 * 2 * 1 = 5! [pronounced fakˈtôrēəl]

Which we can compute rather quickly with a calculator/browser/pre-computed 
tables. Second think how we can remove the choices that we don't want to 
account for (we're not going to pick further than 3) from that number. If we 
can do that we're left with just the number of permutations we are going to
have to count. This can be written as follows::

    5 * 4 * 3 * 2 * 1     120
    -----------------  =  --- = 60
    2 * 1                  2

Interesting right? So the top portion looks like can be written like this::

    (number of choices)!

But what about the bottom **2 * 1**? The remainder can be stated as total
choices minus the choices we're going to make and slap a factorial symbol
on it.

Putting this all together our formula will look like this::

            n!
        ---------
         (n - r)!

And that's all there is to it, for permutations (ORDER MATTERS) then figure out
if repetitions are allowed and if so how to remove the unused permutations.

Combinations
------------
We don't care about positions of each choice! We don't care about the position
of each choice! (like totally!)

Repetitions
-----------
With repetions use the following formula::

     (n + r - 1)!
    --------------
    r! * (n - 1)!


No Repetitions
--------------
If repetitions are not allowed the number of combinations is broken down as
follows::

             n!
        -------------
        r! * (n - r)!

Also known as `Binomial Coefficient`, and this equation is just like
permutations with the added effect of removing the number of time each
combination could be in order


    