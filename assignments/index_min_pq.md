# Overview

In this assignment you will implement an index min priority queue. This is a min priority queue where it is possible to reduce the priority of an existing key. This data structure is a necessary ingredient for an efficient implementation of Dijkstra's algorithm.

In a file `index_min_pq.py`, define a class `IndexMinPQ`. It must provide the following methods:

```python
__init__
is_empty
enqueue
dequeue
reduce_priority
```

The unit tests below give examples of using these methods.

The priority queue is implemented as a min heap. You will also need a dictionary to associate keys with the indices at which they are stored.

**This is an individual assignment. You are meant to write the code on your own. You are welcome to discuss *ideas* with other students (including on the class email list), but don't look at their code or show them yours.**

# Files

* [test_index_min_pq.py](../test/test_index_min_pq.py)

# Hints
Decide in advance whether your heap indices are zero-based or one-based.

Get the min priority queue working (passing most of the tests) before adapting it to allow for reducing priorities.

Store two-item lists in the heap. That way, you can simply compare them to find the lower-priority item. Lists, rather than tuples, are appropriate here because the `reduce_priority` method will modify them.

You don't need a separate size attribute if you use the length of your data list. If you are using one-based indexing, take that into account (because an empty queue will have a list of one ignored item).

To remove an item from a list, use the `pop` method.

Swapping two items requires also updating their entries in the dictionary. It's convenient to write a `_swap` method that does all the work to swap the keys at two given indices.

# Optional Challenge Problems
As described, `enqueue`'s behavior is not well-defined if someone inserts two keys that (a) have the same priority and (b) are instances of a class that doesn't support comparison. Update your data structure to prevent this by storing a *three*-item list for each key: the priority, a count, and the key itself. The count is simply the value of a variable that is updated each time a key is inserted. This breaks ties so that the keys themselves are never compared.

Make your data structure "truthy" so that an empty `IndexMinPQ` will count as `False`, but a nonempty one will count as `True`.

Make your class iterable so that someone could iterate through all of the keys in increasing priority order. For an even greater challenge, make it so that iterating through an `IndexMinPQ` does not remove keys from the queue.

# What to Hand in
Hand in a single file `index_min_pq.py`, containing the definition of `IndexMinPQ`.
