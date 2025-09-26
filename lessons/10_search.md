# Linear search (brute force)
* Idea
* TPS: Best, average, amortized, and worst-case analysis
* TPS: Does sorting the array help?
  * A little; by stopping early you could gain a factor of 2 in speed if key not present

# Binary search (divide and conquer)
* Idea -- requires that the array be sorted
* [search.py](../src/search.py)
* I got the algorithm right on the first try, but used the wrong division operator and forgot to return an index instead of a bool
* `mid = lo + (hi - lo) // 2` to avoid integer overflow
* Show this off if you’re asked to implement binary search in an interview!
* TPS: worst-case analysis
  * Each pass through the loop divides it in half, so it’s logarithmic
* TPS: best-case analysis
  * Constant
* Average case is also logarithmic because most array elements are “leaves”
* TPS: can we use linear search, binary search, neither, or both with a linked list?
  * Both, but binary search becomes less efficient -- linearithmic, because it’s linear time to find each element

# Interpolation search (divide and conquer)
* Assume data are approximately uniformly distributed and make a more educated guess as to where to look first
* Linear time in the worst case but $O(\log \log n)$ on average -- very close to constant
* If time, time these algorithms empirically
