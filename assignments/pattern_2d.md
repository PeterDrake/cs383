# Overview
In your future life as a computer scientist, you will sometimes be asked to solve a problem that is similar (but not identical) to one you've seen before. This particular problem is similar to string matching. You will also get practice comparing the efficiency of different algorithms for the same problem.

**This is a team assignment. When you are done, *one* member of your team should submit the file, including (as a comment at the top of the file) the names of everyone who contributed.**

## The Task
This assignment asks you to implement two algorithms for two-dimensional pattern matching&mdash;the computational equivalent of [Where's Waldo?](https://en.wikipedia.org/wiki/Where%27s_Wally%3F). Specifically, each of your algorithms must find the row and column where (if at all) an $m \times m$ pattern appears in an $n \times n$ text. You may assume that each element in the pattern or text is a 32-bit unsigned integer.

## Brute Force Algorithm
The brute force algorithm checks each $m \times m$ region in the text to see if it matches the pattern. It should quit early if it finds a match. It should also give up on a region as soon as it determines that the region does not contain a match.

Implement this algorithm as a function `match` (taking the pattern and text as arguments, each a list of lists). Put it in the file `brute_force_match.py`.

## Fingerprinting Algorithm

A more clever algorithm using the "transform" strategy computes a hash code (a "fingerprint") for the pattern and for each $m \times m$ region of the text. If the pattern fingerprint doesn't match the region fingerprint, it is known immediately that there is no match. If they do match, the match must be verified by looking at each element of the region.

By itself, this wouldn't save any time; computing the fingerprint would require looking at each element of the region. The clever insight is that, once one region fingerprint is computed, the fingerprint for an overlapping region can be computed without inspecting every element of the new region.

Specifically, the fingerprint is computed by combining all of the elements in a region using bitwise xor. To find the fingerprint for the next region over (say, one column to the right), simply xor together the old fingerprint, the elements on the left edge of the old region, and the elements on the right edge of the new region.

Implement this algorithm as a function `match` (taking the pattern and text as arguments, each a list of lists). Put it in the file `fingerprint_match.py`.

# Files
* [test_brute_force_match.py](../test/test_brute_force_match.py)
* [test_fingerprint_match.py](../test/test_fingerprint_match.py)
# Hints
You'll want some additional functions. If you have a method that is too long to fit on one screen, break it into pieces.

Draw some pictures of examples.

On extremely rare occasions, the random arrays in the test might contain a spurious match, which would cause the test to fail. If you think your code is correct and a test fails, run the test again.

Implementing the fingerprinting algorithm and answering the last analysis question will take some time. Start early!

# Optional Challenge Problems
Learn to use [NumPy](https://numpy.org/), the Python library for numerical computing. Implement these algorithms for NumPy arrays. Include unit tests to verify that your functions are correct.

The official site linked in the previous paragraph has a useful "learn" section. Another good resource is Part II of VanderPlas, *Python Data Science Handbook, 2nd Edition* ([full text online](https://ebookcentral.proquest.com/lib/lewisclark/detail.action?pq-origsite=primo&docID=30285041)).

# What to Hand in
Hand in your files `brute_force_match.py` and `fingerprint_match.py`. Be sure to include the full names of all of your team members in a comment at the top of `brute_force_match.py`.

In a separate document called `match_analysis`, hand in your answers to the following questions:

1. In terms of $m$ and $n$, what is the order of the worst case running time for these algorithms? (It's the same for both of them.)
1. How much actual time does it take to run each of the test cases? (PyCharm will give you this information when you run the tests. For accurate measurements, you should ideally have nothing else running on your computer when you run the tests.)
1. One algorithm performs much better on dense arrays (which are full of random numbers) and the other performs much better on sparse arrays (where almost all of the elements are zero). Which is which and how do you explain this behavior?
