# Overview
In this assignment you will implement and analyze the bubble sort. There are many sorting algorithms, almost all of them more efficient than this one. I want you to have experience implementing one of them; this one is relatively simple. This assignment also gives you practice in the important skill of translating a description of an algorithm into working code.

**This is an individual assignment. You are meant to write the code on your own. You are welcome to discuss *ideas* with other students (including on the class email list), but don't look at their code or show them yours.**

## The Task
Define a function `bubble_sort`. It takes a list as an argument and sorts that list in place (rather than returning a new list).

In a comment, state the worst-case running time of this algorithm.

## Algorithm Description
At any given time, the left part of the array is unsorted and the right part is sorted. Initially the entire array is unsorted. The first pass through the (outer) loop described below moves the largest key into the last place in the array. Now the sorted region consists of that one position. The second pass moves the second largest key into the place before that, so the sorted region now contains the two largest keys, in order. This continues until the entire array is sorted.

Do the following $n - 1$ times:

* Work up through the array from position 0 to the last position in the unsorted region, comparing adjacent elements and swapping if the larger element appears first.

# Files
* [test_bubble.py](../test/test_bubble.py)

# Hints
Your function should have two loops, one nested inside the other. For loops, rather than while loops, are appropriate here.

Working through some examples with pencil and paper, or with playing cards, can help keep your indices straight.

A visualization of the algorithm in action can be found here:

[https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html](https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html)

# Optional Challenge Problems
When you swap two list elements, instead of creating a temporary variable, take advantage of Python's multiple assignment feature.

Add an optional argument `key` that allows you to, for example, sort a list of strings either lexicographically or by length. It should work like the optional argument in the built-in `sort` function.

Suppose you had reason to believe that, in your application, the list passed to the function is often (but not always) already in reverse order. Provide a second version of the function that detects this situation and, when it occurs, sorts the list in linear time.

# What to Hand in
Hand in a single file `bubble.py` containing your definition of bubble_sort. Remember to include the worst-case running time in a comment.
