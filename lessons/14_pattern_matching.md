# Pattern matching
* Problem: first occurrence of a pattern in a text
  * Example 1: “ac” appears at position 3 in “abracadabra”
  * Example 2: “woodchuck” appears at position 22 in “How much wood would a woodchuck chuck if a woodchuck could chuck wood?”
* Brute force: try each possible location, checking character by character
  * In teams, implement it
    * What if it’s not there? Return -1
    * After, make sure it works if pattern is not present or is present at last possible index
  * Analysis: $\Theta(mn)$ in the worst case, where $n$ is length of text and $m$ is length of pattern
    * More precisely, $m * (n - m + 1)$: $m$ comparisons per position, $n - m + 1 positions$
    * $\Theta(m + n)$ on average (because you can rule out most positions almost immediately)
  
* Horspool’s algorithm (transform)
  * Notice that when you find a mismatch you might know immediately, from looking at the pattern, that the next position can’t work
    * Idea: if we check each position starting from the *right end of the pattern*, we sometimes know (without looking at $m$ characters of the text) that we can shift over a bunch
      * Example: looking for “woodchuck”, we find the corresponding chunk of the text ends in a space; we can immediately shift over nine places!
      * Detail: if we’re looking for “woo”, we can only shift over one space when we get to “ wo”.
    * Plan: make a shift table with a number for each character that appears in the pattern. That number answers the question: if I find this character in the text at some position `i`, but don't find a complete match ending at position `i`, how far can I safely shift the pattern to the right (without risking skipping over a match)?
      * Table for woo is w:2, o:1
      * Algorithm:
        1. Use `m` as the default entry
        1. For `i` = 0 through `m` - 2, `table[pattern[i]] = m - 1 - i`
          * Some table entries can be written more than once, so this part is an incremental algorithm
      * Class: work out table for woodchuck
        * w: 8, o: 6, d: 5, c:1, h: 3, u: 2
      * Using this table, look for “woodchuck” in “How much wood would a woodchuck chuck if a woodchuck could chuck wood?”
    * Analysis:
      * Still $\Theta(mn)$ in the worst case
        * This happens when searching for `azzzzz` in a string of `z`s
          * You can only shift over 1 when looking at a `z`, but you have to search back through the entire pattern to realize that the pattern didn’t match here
          * The more complicated Boyer-Moore algorithm improves on this
        * Clearly faster than brute force as it avoids many comparisons
        * $\Theta(n)$ on average for random texts

* Practical Python solution: find method on strings
