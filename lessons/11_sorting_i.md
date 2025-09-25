**Bring: giant playing cards**

# Sorting Problem
* [Video of hermit crabs](https://www.youtube.com/watch?v=f1dnocPQXDQ)
  * This is a priority queue, not a FIFO queue

# Selection Sort
* Idea (demonstrate with cards): repeatedly find the smallest key and put it into place
* Implementation: [sorts.py](../src/sorts.py)
* Analysis: $n^2$ best and worst case

# Bubble Sort
* Idea: $n-1$ bubbling passes, each of which moves the next largest key to the sorted region at the end by swapping adjacent inversions on the way from 0 to that position
* Implementation left as an assignment
* TPS: Analysis 
  * Also $n^2$

# Insertion Sort
* Idea: insert each key in turn into the sorted region
* Implementation
  * Could be improved slightly by not writing the key being inserted until its place is found; left as an exercise
* TPS: Analysis
  * $n^2$ worst and average, but $n$ best
* This is the best of these three
* Good to use when arrays are likely to be nearly sorted or (because it’s simple) very short

If time, play with visualizations from
https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html
