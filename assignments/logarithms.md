# Overview
This (hopefully!) simple assignment is meant to warm up your mathematical and programming muscles. It is also a smoke test of the technology (development environment, handin system, etc.); if there’s a problem, we want to know before things get hairy!

In this assignment you will write a single function to compute a logarithm. Specifically, `log(a, b)` should return the base `a` logarithm of `b`, rounded down to the nearest integer. Your function assumes `a` and `b` are positive integers.

While more sophisticated techniques exist, your function should be based on the idea that `log(a, b)` is the number of times you have to divide `b` by `a` to get down to 1. Use a loop rather than any functions from the `math` module. Because the result will not be an exact integer in some cases, you should divide until you get below 1, then subtract 1 from your count of divisions.

**This is an individual assignment. You are meant to write the code on your own. You are welcome to discuss *ideas* with other students (including on the class email list), but don't look at their code or show them yours.**

# Files
* [test_log.py](../test/test_log.py)

# What to Hand in
Hand in a single file `log.py`. It should contain a single function `log`.
