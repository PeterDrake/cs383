# Overview
This assignment challenges you to implement [Horspool's algorithm](https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore%E2%80%93Horspool_algorithm), a sophisticated algorithm using the “transform” strategy. It is not immediately obvious that this algorithm solves the problem or that it does so efficiently. Getting this algorithm through your head with enough precision to produce a working implementation is a notable achievement.

Define a class `HorspoolStringMatcher` that provides a method `match`. The pattern is provided as an argument to the initializer, which creates the shift table. The text is provided as an argument to `match`, which returns the first index where the pattern appears in the text, or -1 if it does not appear.

`HorspoolStringMatcher` should also provide a method `_get_shift`, which takes a character and returns the shift value for that character. (The leading underscore indicates that this method is "private", as users of this class normally wouldn't access it, but the tests can call it.)

**This is an individual assignment. You are meant to write the code on your own. You are welcome to discuss *ideas* with other students (including on the class email list), but don't look at their code or show them yours.**

# Files
* [test_horspool.py](../test/test_horspool.py)

# Hints
The pattern should be stored as an attribute.

A dictionary is a reasonable way to store the shift table. You can avoid storing the "default" value and simply return that from `_get_shift` when a character isn't found in the table.

# Optional Challenge Problems
Write code to generate random patterns and texts that contain those patterns, then time the algorithm on various lengths. Hand in, as a separate file, a table of your results.

Devise a class of patterns and texts for which this algorithm performs poorly and verify this empirically.

# What to Hand in
Hand in your file `horspool.py` containing the definition of `HorspoolStringMatcher`.

