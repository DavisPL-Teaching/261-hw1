# ECS 261 Homework 1: Writing Specifications in Hypothesis and Z3

## Due date: Friday, April 18 at 11:59pm

There are four parts to this homework. The first part explores writing specifications in Hypothesis, and the second part explores writing specifications in Z3. The third part is a program using Z3 to solve the 4 numbers game, and the fourth part explores limitations of Z3.

## Getting started

To get started, make sure you have completed Homework 0.
in particular, you should have Python, Hypothesis, Pytest, and Z3 installed.
Please submit the homework through Gradescope.

Then open and edit the files `part1.py`, `part2.py`, `part3.py`, and `part4.py`.
To run the code, you can use
```shell
pytest part1.py
pytest part2.py
pytest part3.py
pytest part4.py
```

## Grading notes

- Don't change the function signatures unless you are asked to do so. This ensures that our gradings scripts will work correctly.

- Please do not modify the file names or the list of `test_` functions in parts 1, 2, and 4, as your results will be compared with the official rubric. If you want to add other tests, remember to comment them out after.

- If your code is correct, **there should be no pytest failures (shown in red)** -- instead, you should be using the annotation `pytest.mark.xfail` to mark tests that are expected to fail. These will show up in yellow.

- Make sure your answers to free response questions are between the `===== ANSWER HERE =====` and `===== END ANSWER =====` markers.

- We won't be able to grade code that doesn't run, so please make sure that your code runs before submitting. You should be able to run `pytest <yourfile>.py` and see a list of successful, skipped, and expected failing test cases. If you have some broken code, please remember to comment out the broken parts (or use `@pytest.mark.skip` to the unit tests) to ensure you receive some partial credit.
