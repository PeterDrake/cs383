# Heap
* Motivation: priority queue

## Heap invariant
* Heap invariant
  * Complete binary tree
  * Every node >= its children
    * This is a max-heap; a min-heap is also possible
  * TPS: What can you say about the positions in the tree of the smallest and largest keys?

## Array representation
* Work out rules for
    * Parent
        * Zero-based: $\lfloor{(i-1) / 2}\rfloor$
        * One-based: $\lfloor{i / 2}\rfloor$
            * We’ll go with one-based, as it makes the formulas simpler and faster
    * Left child: $2i$
    * Right child: $2i + 1$
      * How do you know if an index is part of the tree? 

## Heapify operations
* Swim
  * While node > parent, swap with parent and swim the parent
* Sink
  * While node < child, swap with larger child (why?) and sink that child

## Priority queue implementation
* Start with empty array (stretching it if necessary)
* Insert
  * Add new key at next available position, then swim
* Delete
  * Swap root (which will be returned) with last key, then sink root
* Perform a few insertions and deletions
* Both operations take logarithmic time because the tree is complete 

## Heapsort
* Construct the heap
  * For $\lfloor{n/2}\rfloor$ down to 1, sink
    * We don’t have to sink the other nodes, because they’re leaves
    * This takes linear time (proof omitted)
* Repeatedly delete
  * Each time this moves the largest element to rightmost slot in the heap, which sorts things
* This takes time in $O(n \log n)$ because of the time to delete, and $\Omega(n \log n)$ by the lower bound on comparison sorts, therefore $\Theta(n \log n)$ time in the worst case. Also can be shown to be linearithmic on average.
* In place, not stable, not as fast as quicksort in practice

## Order statistics
* TPS: How would you find the $k$ smallest elements in an array?

## Python in practicer
* In Python, `queue.PriorityQueue` is a min priority queue
