# A lower bound on sorting
* Comparison sorts (all we've seen so far)
* Sorting trees
* $\Omega(n \log n)$ lower bound (average and worst case)

# Bucket sort
* Assume the data are uniformly distributed across some range
* Make one linear pass allocating them to buckets, sort each small bucket, then concatenate
* [Visualization](https://www.cs.usfca.edu/~galles/visualization/BucketSort.html)
* Linear time on average if assumption is true
* Beats lower bound because this isn't a comparison sort -- we make additional assumptions about the data
* In the worst case, assuming insertion sort is used to sort buckets, takes quadratic time

# Properties of sorting algorithms
* Stability
  * Why we care: sorting a spreadsheet on multiple keys (e.g., first and last name)
  * Stable sorts: insertion sort, mergesort, bucket sort
* In-place
  * Do we need essentially a second copy of the array?
  * Mergesort and bucket sort are not in-place

# Choosing an algorithm
* [Table](https://algs4.cs.princeton.edu/25applications/)
* Note extra space for some algorithms
* [Empirical comparison](https://opendsa-server.cs.vt.edu/OpenDSA/Books/Everything/html/SortingEmpirical.html)
  * Discuss optimizing Quicksort with Insertion Sort
* Discussion: if you could only have one algorithm, which would you choose and why?
* `java.util.Arrays.sort` uses Quicksort for primitives but mergesort for objects. Why?
  * Quicksort is generally faster, but mergesort is stable (which might matter for objects).
  * Look at API
  * You'll almost always use the built-in sort, unless you know something special about your data or have a slightly different problem (like finding the median).
* If time, [xkcd on sorting algorithms](https://xkcd.com/1185/)
