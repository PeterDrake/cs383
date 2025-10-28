# Closest pairs
* Problem definition
* Warmup: everyone implement brute force algorithm using TDD
* Build a larger set of points using a specific random seed and use it to create a new test -- our fancier algorithm will produce the same answer
* Divide and conquer algorithm
  * Idea:
  * Divide the points in half by `x` coordinate
  * Recursively find the minimum distance in each half
    * Let `d` be the lower of these
  * `d` might not be the shortest distance
    * If there is a shorter one, it must straddle the center line
    * We can check through the points near the center line in `y` order
    * Each one only has to be compared to at most 5 others, subsequent in `y` list
      * That's all that will fit into the 2`d` x `d` box above it
  * More detailed algorithm:
    * Sort the points into two lists by their `x` and `y` coordinates respectively
    * Base case:
      * if $n \leq 3$, use brute force
    * Otherwise:
      * Copy each (left, right) half of points in `x`-sorted list into a sublist
        * Copy the same points from the `y`-sorted list into two more sublists
          * Discussion: how might we do this in linear time?
      * Recursively find the minimum distance within each half; `d` = minimum
      * Copy all the points within d of the median onto another list, sorted by `y`
      * For each point in this list in order
        * Find its distance to the next 5 points, reducing `d` if a new low is found
      * Return `d`
  * Analysis
    * $\Theta(n \log n)$ for the sorting
    * $T(n) = 2T(n/2) + n$ for the recursive part
    * $\Theta(n \log n)$
* If time, implement it
