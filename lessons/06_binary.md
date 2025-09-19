# Binary representation
* Class: write a method to convert an int to binary form
* Built-in solutions:
  * Use bin function to convert to binary
  * To convert from binary, start int literal (after any minus sign) with 0b
* Weird Python twist: ints are arbitrarily long!
## Two’s complement
* Idea: to represent a negative number, flip all the bits and then add one
* Why?
  * We don’t want -0
    * But floating point types have it
  * Arithmetic still works, namely a - b == a + -b
  * Demonstrate 7 - 3 with four bits
  * Python doesn't normally show you this, but you can see it: `bin(-6 & 0b11111111)`
    * This works because -6 == ~5
  * In other languages, you have to be careful about shifting with the sign bit
## Bitwise operators
* `&` and
* `|` or
* `^` xor
* `~` complement
* `<<` left shift (* 2^n)
* `>>` right shift (/ 2^n)
## Representing sets with ints
* Write BitVector class allowing us to set or check bits
* TPS: union, passing my test
* TPS: write a test for intersection
* What if we used `^`? Symmetric difference
## Bit-twiddling hacks
* In teams, explain some from https://graphics.stanford.edu/~seander/bithacks.html
  * Be aware that this code is in C, which can have some special syntax, has unsigned integers, and has no Boolean type
  * Detect if two integers have opposite signs
  * Determine if an integer is a power of 2
  * Count bits set, Brain Kernighan’s way
  * Swap value with xor
  * Round up to the next highest power of 2
  * Compute modulus division by 1 << s without a division operator
  * Determine if a word has a zero byte
