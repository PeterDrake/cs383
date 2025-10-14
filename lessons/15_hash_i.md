# Hash tables
* ADT: add, remove, contains
* 10 min in teams: implement a version of the set ADT where the keys are nonnegative integers in [0,100)
  * Have some team members come up with unit tests
  * They should come up with direct addressing tables
* Problem: if universe of possible keys is much larger than set, a lot of space is wasted
  * Solution: use a hash function to map keys to cells in table
* Problem: collisions
  * A good hash function (which distributes the keys evenly) can reduce the number of collisions
  * Collisions are inevitable because of the pigeonhole principle
  * Solution 1: chaining
    * Slight problem: using references wastes some space and hurts cache performance
  * Solution 2: linear probing: store at $h(n) + i$
    * Problem: hitting end of table
      * Solution: wrap around
    * Problem: clustering (including extreme case where table is completely full)
      * Solution: rehash into larger table
        * Best to do this before table is completely full to improve performance

# Implementation
* [hash.py](../src/hash.py)

# Analysis:
* Search (assuming chaining): constant time on average, linear time in unlikely worst case
  * This assumes you rehash into a larger table when it becomes too full
* Insertion and deletion are the same
* … but how to delete safely?
  * Chaining: delete from chain
  * Linear probing: reinsert all items later in probe sequence
