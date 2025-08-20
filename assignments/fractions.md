# Overview
This assignment gives you practice writing Python classes, implementing nontrivial algorithms, and working as part of a team.

Define a class `Fraction` that represents a rational number with a numerator and a denominator (both assumed to be integers). This class should allow you to work with fractions in Python's read-eval-print loop:

```python
>>> a = Fraction(2, 3)
>>> a
2/3
>>> b = Fraction(2, 8)
>>> b
1/4
>>> a + b
11/12
>>> float(a)
0.6666666666666666
```

All of the methods you need to implement are magic methods:

```python
__init__
__repr__
__add__
__sub__
__mul__
__truediv__
__float__
```

**This is a team assignment. When you are done, *one* member of your team should submit the file, including (as a comment at the top of the file) the names of everyone who contributed.**

# Files
* [test_fraction.py](../test/test_fraction.py)

# On Working as a Team
This project is, intentionally, too much for one student to complete in a reasonable amount of time. You will need to work together as a team!

The first thing to work out is communication and scheduling. Exchange email addresses or phone numbers. Set up a group chat or other means of communication. Figure out when you can meet to work on the project. It will take several hours. It's best if you can all work together, but if not, figure out who can work at what times and plan to hand off the code to the rest of the team after each session.

When working, it's a good idea to use [pair programming](https://www.youtube.com/watch?v=rG_U12uqRhE).

Break the problem down into steps. Have one pair (or person) do the first step, then a different pair do the next step, and so on. Here's a good sequence for this assignment:

1. Make sure everyone has the code and can run the tests.
1. Pass `test_represents_simple_fraction`.
1. Pass `test_reduces_to_lowest_terms`.
1. Pass `test_handles_negative_numerator`.
1. Pass `test_handles_negative_denominator`.
1. Pass `test_handles_negative_numerator_and_denominator`.
1. Pass `test_represents_improper_fraction`.
1. Pass `test_adds`.
1. Pass `test_subtracts`.
1. Pass `test_multiplies`.
1. Pass `test_divides`.
1. Clean up the code: remove commented-out code, improve names of local variables, eliminate redundancy, etc.
1. If you have time, save a copy and then consider tackling optional challenge problems.
1. Clean up the code again.
1. Have *one person* hand in your solution with everyone's names on it.

Remember to trade off who is "driving" (typing) after each step. Avoid having someone who never gets a chance to contribute or someone who "heroically" does almost all of the work. If you feel your teammates are more experienced than you, ask questions! If you feel you are more experienced, be patient and remember that making your team stronger is more important than completing the project as quickly as possible.

# Hints
Write as little code as you can to pass the first test, then move on to the next one. You may occasionally find that code written to pass one test happens to pass several more.

The greatest common divisor algorithm is helpful for reducing a fraction to lowest terms.

Subtraction can be defined in terms of addition. Division can be defined in terms of multiplication.

You don't have to override `__str__`, because by default `__str__` calls `__repr__`.

# Optional Challenge Problems
If you get everything working, *have saved a copy just in case*, and want an additional challenge, try some of the following:

* Implement the `__eq__` method so that `==` and `!=` work properly with Fractions.
* Implement the other comparison methods so that `<`, `<=`, `>`, and `>=` work.
* Modify `__eq__` so that `Fraction(6, 3) == 2` and vice versa. In other words, make it so that you can compare your fractions with regular Python numbers.

# What to Hand in
Hand in your file `fraction.py`, containing your definition of the class Fraction. Be sure to include the full names of everyone who worked on the project in a comment at the top of the file.