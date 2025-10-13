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

# Hash codes
* Problem: what if your key isn't a nonnegative integer?
* Hash code
  * Found with hash, composed with the table's hash function
* Some objects cannot be hashed
  * Immutable objects are safe
    * Numbers, strings, tuples
  * Generally mutable objects are not, but there are exceptions (like functions)
    * The part used to compute the hash code has to be immutable
* Defining a `__hash__` method for your own class:
  * By default, it returns the address where the object lives in memory
  * `==` should imply same hash, but not necessarily vice versa
    * Default __hash__ is consistent with default __eq__
  * If you override one, override both
    * Otherwise multiple equal objects could end up in the table
  * __le__ and so forth should also be consistent if your object is comparable
  * To mark your class as unhashable, define __eq__ but not __hash__
* Example: write a `__hash__` method for our Vector class
