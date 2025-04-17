"""
Part 4: Limitations of Z3

This part will explore two limitations of Z3:

1. Sometimes, Z3 gets the right answer, but takes a long time to do so,
    or even hangs indefinitely.
2. Sometimes, Z3 can't prove a statement at all, and returns UNKNOWN.

=== What is the pigeonhole principle? ===

This is a principle that says the following:

"If you have n+1 pigeons and they are in n holes,
then at least one hole has more than one pigeon."

For example, if you put 4 pigeons in 3 holes,
then at least one hole has at least 2 pigeons.

Example:
|     |     |     |
|     |  o  | ooo |
-------------------

Above, the first hole has 0 pigeons, the second hole has 1 pigeon,
and the third hole has 3 pigeons. So the third hole has more than
one pigeon.

We will consider two different encodings of the pigeonhole principle.
The first encoding is for a fixed number of pigeons and holes.
The second encoding is for a general number of pigeons and holes.
These will be examples of limitations (1) and (2) above.
"""

import z3
import pytest

from helper import prove, solve, SAT, UNSAT, PROVED, COUNTEREXAMPLE, UNKNOWN

"""
=== First encoding ===

The first encoding is for a fixed number of pigeons and holes.
You will be asked to write two functions:

1. pigeons_in_holes(m, n):
    Input:
        m is a Python integer (the number of pigeons)
        n is a Python integer (the number of holes)

    Returns:
        A formula that says that there are m total pigeons in n holes.

2. two_in_hole(m, n):
    Input:
        m is a Python integer (the number of pigeons)
        n is a Python integer (the number of holes)

    Returns:
        A formula that is true exactly when at least one hole has at least
        two pigeons.

There are test cases that will help check that
your implementation is correct.
"""

def pigeons_in_holes(m, n):
    # TODO
    raise NotImplementedError

def two_in_hole(m, n):
    # TODO
    raise NotImplementedError

"""
Test cases

Uncomment these to make sure your implementation is working.
"""

@pytest.mark.skip
def test_pigeons_in_holes():
    assert solve(pigeons_in_holes(4, 3)) == SAT
    assert solve(pigeons_in_holes(0, 3)) == SAT
    assert solve(pigeons_in_holes(1, 0)) == UNSAT
    assert prove(pigeons_in_holes(1, 1)) == COUNTEREXAMPLE

@pytest.mark.skip
def test_two_in_hole():
    assert solve(two_in_hole(3, 3)) == SAT
    assert prove(two_in_hole(3, 1)) == COUNTEREXAMPLE

@pytest.mark.skip
def test_combined():
    assert solve(z3.And([
        pigeons_in_holes(1, 2),
        two_in_hole(1, 2),
    ])) == UNSAT
    assert prove(z3.Implies(
        pigeons_in_holes(3, 2),
        two_in_hole(3, 2),
    )) == PROVED

"""
3. Now write a function for the pigeonhole principle,
using the functions you wrote above.

The input is a Python integer n, and it should return
a specification (as a Z3 formula) that says that the
pigeonhole principle is true for n + 1 pigeons and n holes.
"""

@pytest.mark.skip
def pigeonhole_principle(n):
    # TODO
    raise NotImplementedError

"""
Let's test the performance of Z3 on your implementation.
Uncomment the following tests.

4. How long does it take to prove the small and medium versions
on your machine?
(list the number of seconds or a timeout if it takes too long):

===== ANSWER Q4 BELOW =====

===== END OF Q4 ANSWER =====

5. What happens when as increase the number of holes to
tens of thousands (the "large" test)?
(list the number of seconds or a timeout if it takes too long):

===== ANSWER Q5 BELOW =====

===== END OF Q5 ANSWER =====

Make sure that your final code has @pytest.mark.skip only for the tests
which time out, otherwise the test should pass.
"""

@pytest.mark.skip
def test_pigeonhole_principle_small():
    for n in range(1, 11):
        assert prove(pigeonhole_principle(n)) == PROVED

@pytest.mark.skip
def test_pigeonhole_principle_medium():
    assert prove(pigeonhole_principle(1000)) == PROVED
    assert prove(pigeonhole_principle(2000)) == PROVED
    assert prove(pigeonhole_principle(3000)) == PROVED

@pytest.mark.skip
def test_pigeonhole_principle_large():
    assert prove(pigeonhole_principle(10_000)) == PROVED
    assert prove(pigeonhole_principle(20_000)) == PROVED
    assert prove(pigeonhole_principle(30_000)) == PROVED

"""
=== Second encoding ===

Here is a version of the pigeonhole principle
that is general enough to work for any n, instead of
just a specific n.

This encoding is given to you.
It uses an unbounded array (z3.Array) to create
an arbitrary number of holes.
"""

def pigeonhole_principle_general():
    # The number of holes
    n = z3.Int('n')
    # The list of n holes
    holes = z3.Array('holes', z3.IntSort(), z3.IntSort())
    # An array that stores the sum of the first i holes,
    # for all i from 0 to n
    sum_holes = z3.Array('sums', z3.IntSort(), z3.IntSort())

    # Sum constraints
    sum_base_case = sum_holes[0] == 0
    i = z3.Int('i')
    sum_inductive = z3.ForAll(i, z3.Implies(
        z3.And(i >= 0, i < n),
        sum_holes[i + 1] == sum_holes[i] + holes[i]
    ))

    # Positivity constraint
    # Note: this is technically unnecessary
    # (since the principle holds even with negative pigeons in holes).
    positive = z3.ForAll(i, z3.Implies(
        z3.And(i >= 0, i < n),
        holes[i] >= 0
    ))

    # Pigeonhole principle
    pigeons_in_holes = sum_holes[n] == n + 1
    two_in_hole = z3.Exists(i, z3.And(i >= 0, i < n, holes[i] >= 2))

    # Putting everything together
    return z3.Implies(
        z3.And([
            n >= 0,
            sum_base_case,
            sum_inductive,
            pigeons_in_holes,
        ]),
        two_in_hole,
    )

"""
What happens when we ask Z3 to prove the general pigeonhole
principle?

6. Uncomment the following test.
If it fails, change PROVED to the expected result.

===== ANSWER Q6 BELOW =====

===== END OF Q6 ANSWER =====
"""

@pytest.mark.skip
def test_pigeonhole_principle_general():
    assert prove(pigeonhole_principle_general()) == PROVED

"""
Just to be sure we haven't made a mistake,
we can also try to run a version
of the pigeonhole principle that is *not* true, to see if Z3
can find a counterexample.

7. Copy and paste the pigeonhole_principle_general code,
but make a small change somewhere in the
function so that it is false.

Then, uncomment the test which asserts that
    prove(pigeonhole_principle_false()) == COUNTEREXAMPLE.
This test should pass.
"""

def pigeonhole_principle_false():
    # TODO: Copy and paste the previous function.
    # Modify one of the constraints so that the principle is false.
    raise NotImplementedError

@pytest.mark.skip
def test_pigeonhole_principle_false():
    assert prove(pigeonhole_principle_false()) == COUNTEREXAMPLE

"""
8. Is the result what you expected?
Why do you think Z3 has trouble with this problem?
Comment on your thoughts below.

===== ANSWER Q8 BELOW =====

===== END OF Q8 ANSWER =====
"""
