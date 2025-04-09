"""
Part 1: Writing specifications with Hypothesis
"""

from hypothesis import given
from hypothesis import strategies as st
import pytest

"""
A. Writing specifications

Consider the absolute value function:
"""

def abs(x):
    if x >= 0:
        return x
    else:
        return -x

"""
Write a specification for the following properties using Hypothesis:

1. If x is greater than or equal to 0, then the absolute value of x is equal to x.

2. If x is less than y, then the absolute value of x is less than the absolute value of y.

3. If x is equal to y + 1, then the absolute value of x is equal to 1 plus the absolute value of y.

4. The absolute value applied twice (absolute value of the absolute value of x) is equal to the absolute value of x.

5. The absolute value of (x + y) is less than or equal to (the absolute value of x) + (the absolute value of y).

- To run the test after implementing it, remove the skip annotation:
@pytest.mark.skip(reason="Unimplemented")

- If the property does not hold, add the annotation
@pytest.mark.xfail(reason="The property is not true")
to tell pytest that the test is expected to fail.
We will use this during grading to check if you have correctly identified the properties!

The first specification is written for you.

You should pick a @given annotation for each property that makes sense
for the property in mind, and use assert() statements to check the property.
You may also choose to use assume() statements also if you find them helpful.
"""

@given(
    st.integers(min_value=0, max_value=1000),
)
def test_abs_1(x):
    assert abs(x) >= x

@pytest.mark.skip(reason="Unimplemented")
# @given(...)
def test_abs_2(x, y):
    # TODO
    raise NotImplementedError

@pytest.mark.skip(reason="Unimplemented")
# @given(...)
def test_abs_3(x, y):
    # TODO
    raise NotImplementedError

@pytest.mark.skip(reason="Unimplemented")
# @given(...)
def test_abs_4(x):
    # TODO
    raise NotImplementedError

@pytest.mark.skip(reason="Unimplemented")
# @given(...)
def test_abs_5(x, y):
    # TODO
    raise NotImplementedError

"""
B. Stronger and weaker specifications.

6. Write two of your own specifications for the abs() function which satisfy the following:

- The first specification should be *weaker* than the second one.
  That is, any program satisfying the first spec should satisfy the second.

- The first specification should be true for abs() and the second should be false for abs().
"""

@pytest.mark.skip(reason="Unimplemented")
# @given(...)
def test_abs_6_weaker(x):
    # TODO
    raise NotImplementedError

@pytest.mark.skip(reason="Unimplemented")
# @given(...)
def test_abs_6_stronger(x):
    # TODO
    raise NotImplementedError

"""
Now answer the following questions:

7. Is it possible to have an implementation of abs() that is the other way around, i.e. passes your stronger spec and fails the weaker one?

===== ANSWER Q7 BELOW =====

===== END OF Q7 ANSWER =====

8. Is it possible to have an implementation of abs() that is different than the correct implementation, but still passes the same set of specs
(i.e., passes all the specs we considered so far that passed for abs?
If so, give an example, if not, state why not.

===== ANSWER Q8 BELOW =====

===== END OF Q8 ANSWER =====
"""

# Example here
def q8_example():
    # TODO
    raise NotImplementedError

# If so, write a test that shows it passes the tests so far
# (Otherwise, leave the code below as skipped and change the reason= annotation)
@pytest.mark.skip(reason="Unimplemented")
# @given(...)
def test_q8(x):
    # TODO
    raise NotImplementedError

"""
C. Writing specifications, continued

Write a specification in Hypothesis for the following two functions.

9. pad_with_spaces

10. split_in_half

Your specifications should completely describe the behavior of the function
on all possible inputs.
The @given annotations are written for you.

Clarification on "Completely describe the behavior of the function":
this means that you should take the output of the function, and check that every piece of data in it was computed correctly.
It may feel like you are re-implementing the logic of the function in some parts, that's OK.

(Note: this is called "functional correctness" or "complete functional correctness" - in the context of program verification, it means verifying for every input that the output was computed correctly for that input.)
"""

def pad_with_spaces(s, n):
    """
    Given a string s and an integer n, returns a string that is
    n characters long, with s on the left and spaces on the right.
    If s is longer than n, returns None.
    """
    if len(s) > n:
        return None
    return s + " " * (n - len(s))

@pytest.mark.skip(reason="Unimplemented")
@given(
    st.text(),
    st.integers(min_value=0, max_value=1000),
)
def test_pad_with_spaces(s, n):
    # (In Python, a better style than using 'pass' to indicate unimplemented
    # functions is to raise a NotImplementedError exception.
    # We will use this style in the rest of the file. Remove the following
    # line once you have implemented the test.)
    # TODO
    raise NotImplementedError

def split_in_half(s):
    """
    Given a string s, returns a tuple of two strings, where the first string
    is the first half of s and the second string is the second half.
    If the length of s is odd, the first string is one longer than the second.
    """
    mid = (len(s) + 1) // 2
    return s[:mid], s[mid:]

@pytest.mark.skip(reason="Unimplemented")
@given(st.text())
def test_split_in_half(s):
    # TODO
    raise NotImplementedError

"""
11. Modify split_in_half to introduce an off-by-one error.
(There are multiple ways to do this, so you can choose any one you like.)

Check that the same test you wrote above catches the bug
(fails on the buggy implementation).

Trivia:
If you wrote your specification correctly, *any* program that has a
different output from the correct implementation -- even on a single input --
should fail to satisfy the specification!
This type of specification is called a "strongest postcondition"
because it is the strongest property (the most specific) that must hold after
the function is executed.
We will learn more about strongest postconditions in the program verification
part of the course.
"""

def split_in_half_buggy(s):
    # TODO
    raise NotImplementedError

@pytest.mark.skip(reason="Unimplemented")
@given(st.text())
def test_split_in_half_buggy(s):
    # TODO
    raise NotImplementedError

"""
D. Exploring preconditions: Fahrenheit-Celsius conversion

The next few exercises are about playing with preconditions.
Preconditions are the input constraints inside
the @given annotations that we have been writing.
We will use Hypothesis preconditions to determine the
set of inputs for which a certain property holds.

Here is a popular "mental math" trick to convert Fahrenheit to Celsius:
Subtract 30 from the Fahrenheit temperature and divide by 2.
Example: 70 degrees Fahrenheit is approx. (70 - 30) / 2 = 20 degrees Celsius.
(You can also do the reverse to convert Celsius to Fahrenheit.)

Below, we provide a conversion function both ways that uses this trick.
For simplicity, we round the input/output of both functions to the nearest
integer, using the built-in `round` function.
(It rounds to the nearest even number in case of a tie -- e.g. round(2.5) = 2.)

We also provide the "true" conversion functions that use the exact formula,
and these also round to the nearest integer.
"""

def f_to_c_v1(f):
    return round((f - 30) / 2)

def c_to_f_v1(c):
    return round(c * 2 + 30)

def true_f_to_c(f):
    return round((f - 32) * 5/9)

def true_c_to_f(c):
    return round(c * 9/5 + 32)

"""
12. Use Hypothesis to determine for which inputs the conversion above
(the _v1 functions) is close to correct: within an error of 5 degrees.

For simplicity, assume the input/output for all functions are integers!
Don't worry about floating point inputs. (That is also why the outputs above
are rounded.)

The interesting part here is the @given annotation --
you should play with the minimum and maximum values
    min_value=...
    max_value=...
to see for which *integers* the test passes.
Your final answer should have a @given annotation with the minimum integer
as small as possible and the maximum integer as large as possible,
such that the test passes.

Note: you may need to change max_examples to get some tests to fail reliably.
You can do that by adding:
from hypothesis import settings
@settings(max_examples=500)
which we have added for the tests below.
By default, only 100 examples are tested.

Remember to remove @pytest.mark.skip(reason="Unimplemented")
once you have implemented each test.
"""

from hypothesis import settings

@pytest.mark.skip(reason="Unimplemented")
# @given(st.integers(..))
@settings(max_examples=500)
def test_f_to_c_v1(f):
    # TODO
    raise NotImplementedError

@pytest.mark.skip(reason="Unimplemented")
# @given(st.integers(..))
@settings(max_examples=500)
def test_c_to_f_v1(c):
    # TODO
    raise NotImplementedError

"""
13. Here is a more precise trick:

For F to C, subtract 32, then divide by two, and let that result be x.
Then compute x / 10 (float division) and add it to x.
Round the result to the nearest integer.
Example:
68 F -> 68 - 32 = 36 -> 36 / 2 = 18 -> 18 / 10 = 1.8 -> 18 + 1.8 = 19.8 -> 20 C.

For C to F, multiply by 2, and let that result by x.
Then compute x / 10 (integer division) and subtract it from x.
Finally, add 32, and round to the nearest integer.
Example:
20 C -> 20 * 2 = 40 -> 40 / 10 = 4 -> 40 - 4 + 32 = 68 F.

Implement both functions, then use Hypothesis to check for which inputs
the conversion is close to correct: within 1 degree of the true conversion.
"""

def f_to_c_v2(f):
    # TODO
    raise NotImplementedError

def c_to_f_v2(c):
    # TODO
    raise NotImplementedError

@pytest.mark.skip(reason="Unimplemented")
# @given(..)
# @settings(max_examples=500)
def test_f_to_c_v2(f):
    # TODO
    raise NotImplementedError

@pytest.mark.skip(reason="Unimplemented")
# @given(..)
# @settings(max_examples=500)
def test_c_to_f_v2(c):
    # TODO
    raise NotImplementedError

"""
14. We would also like it to be true that converting from C to F,
followed by converting back from F to C, gives the original value.
x -> convert to F -> convert to C -> x
Similarly:
x -> convert to C -> convert to F -> x

Assume that we can tolerate an error of 1 degree in the final result.
Write a test that checks both properties using Hypothesis,
and find the smallest and largest values for which the property holds.
Use the more precise _v2 versions for this problem.
"""

# @given(..)
# @settings(max_examples=500)
@pytest.mark.skip(reason="Unimplemented")
def test_f_to_c_to_f(x):
    # TODO
    raise NotImplementedError

# @given(..)
# @settings(max_examples=500)
@pytest.mark.skip(reason="Unimplemented")
def test_c_to_f_to_c(x):
    # TODO
    raise NotImplementedError
