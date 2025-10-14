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
* What's a good hash code?
  * Your goal is to make all hash codes equally likely, not to avoid collisions altogether (which would be impossible)
  * Try to use all bits
    * Convenience store prices example
  * Beware of anagrams
    * Just xoring the bits from characters of a string gives the same hash code for anagrams
      * Shifting fixes this
  * Reasonable Python solution: put the parts you care about into a tuple and hash them
    * Unsure? Plot the distribution

# Python practice
* Why not use hash tables for all sets and dictionaries?
  * Can't do ordered traversal, min, max, range searches
* Python sets and dictionaries use hash tables
  * This means keys must be hashable
* Python hashes are not the same from one run to the next!
  * https://stackoverflow.com/questions/27522626/hash-function-in-python-3-3-returns-different-results-between-sessions

# Experience with computer Go
* Zobrist hashes for ko
* How to make a number positive (bitwise-and it with `MAX_VALUE`)
* Collisions are so rare that you just ignore them!
