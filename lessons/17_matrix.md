**Bring Levitin**

# Dot product
* Idea
* Implement it

# Matrix multiplication
* Motivation: state machine modeling (e.g., pandemics), neural networks, graphics
* Idea / example
  * RC joks
* TPS: What constraints are there on the sizes of the matrices?
* Everyone individually implement obvious brute force algorithm for square matrix
* Analysis: $n^3$, where $n$ is width of matrix
* Place your bets: everyone write down a lower bound order. You want to get as close as possible to the fastest known algorithm without going over.

# Multiplying large integers (divide and conquer)
* Relevant to cryptography
* Example from ***Levitin 187***
* Saves a multiplication
  * Formula for two digits
  * Same trick works for first and second half of a long number
  * Analysis:
    * $T(n) = 3T(n/2)$, where $n$ is number of digits
    * Solve by backward substitution, Levitin 188
    * Works out to $3^(log2(n)) = n^(log2(3))$, which is roughly n^1.585
    * Better than the $n^2$ required by the grade school algorithm
    * (Number of additions/subtractions increases, but it’s in the same order)
  * If time, introduce Master Algorithm, Levitin 171
