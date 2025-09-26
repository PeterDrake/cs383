# Divide-conquer-recombine model

# Mergesort
* Idea: cut in half, recursively sort, merge
  * Playing card demonstration
  * Here the recombining is the hard part
* Implementation
  * `sort` calls `f`, which is recursive and calls `merge`
  * Watch `merge` work with cards
    * Write variables on board instead of cards
  * How long does `merge` take (if there are $n$ keys in the `lo..hi` range)?
    * Linear
  * Recurrence for merge sort: $T(1) = 1$, $T(n) = n + 2T(n/2)$, assuming $n$ is a power of 2
    * Without this assumption, you’d need floors and ceilings, but it doesn’t change order of the result
    * Solution to come
* Visualization if time: https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html

# Quicksort
* Idea: partition into small and large numbers, then recursively sort each piece
  * Playing card demonstration
  * Here the *dividing* is the hard part
* Implementation
  * Mystery foreshadowing: why shuffle first?
  * First `sort` calls `f`, which is recursive
  * How long does partitioning take?
    * Linear
    * There are faster, in-place algorithms
  * Recurrence: same as before if the partition is even. If it’s extremely uneven, $T(1) = 1$, $T(n) = n + T(n-1)$.
    * Solution to come
* Visualization if time:
* https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html
  * This uses a fancier partitioning algorithm
  * Stepping can be useful
  * If no time, note that some visualizations use slightly different partitioning algorithms.

# Solving recurrences
* Solving means finding an equivalent equation with $T$ only on the left
* Five examples, all with $T(1) = 1$:
  * $T(n) = 1 + T(n-1)$
  * $T(n) = n + T(n-1)$
  * $T(n) = 1 + T(n/2)$
  * $T(n) = n + T(n/2)$
  * $T(n) = n + 2T(n/2)$
* Techniques
  * Forward substitution
    * $T(1) = 1$
    * $T(2) = 1 + 1$
    * $T(3) = 1 + 1 + 1$
    * …
    * $T(n) = n$
  * Verify by plugging in:
    * $T(n) = 1 + T(n-1)$
    * $n \stackrel{?}{=} 1 + (n - 1)$
    * $= n$
  * Also do second one, getting $n(n+1)/2$
  * Assign teams to solve the other three (assuming $n$ is a power of 2)
    * $1 + log2(n)$
    * $2n - 1$
    * $n(1 + log2(n))$

# Analysis of these sorting algorithms
* Mergesort takes time in $\Theta(n \log n)$
* Quicksort takes time in $\Theta(n \log n)$ in the best case (and, it turns out, on average), but $\Theta(n^2)$ in the worst case
* Shuffling (TPS if time) means no particular input guarantees worst-case performance
