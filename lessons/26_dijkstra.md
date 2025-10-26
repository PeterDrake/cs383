# Dijkstra's algorithm
* Problem: find the shortest path (in terms of total edge cost) between two vertices in a weighted, directed graph with nonnegative edge weights
  * Simple example where fewest edges is not shortest path
  * It turns out to be just as easy to find the shortest path to every other vertex, although you can stop early if you only care about one
  * Negative weights raise the possibility of negative cycles, which would mean there is no shortest path
  * TPS: If I had a solution to this problem, how could I use it for an undirected graph?
* Plan: an incremental algorithm
  * Initially, for each vertex, set `distance_to` to infinity and `edge_to` to None
  * For the start vertex, set `distance_to` to 0
  * Put the start vertex into a min priority queue with priority 0
  * While the queue is not empty:
    * Pull out the lowest-priority vertex
    * Relax each edge out of this vertex
* What does relax mean?
  * Initially, we have the hard constraint that no edges are allowed
    * Our initial distances (0 for start, infinity elsewhere) are correct
  * Relaxing an edge means updating the distances to allow this edge (relax the constraint that it's not allowed)
  * Algorithm:
    * if `distance_to[v] + edge weight < distance_to[w]`:
      * Update `distance_to[w]`
      * Update `edge_to[w]`
      * Add `w` to the priority queue
* Work through larger example
* Analysis: $\Theta(E \log E)$ in worst case
  * Each edge is relaxed at most once and each relaxation requires a heap operation
  * There are at most $E$ insertions into the queue
  * Improvement: use an index priority queue where we can update the priority of an item
    * This gets us to $\Theta(E \log V)$, because each vertex is inserted at most once
* Mob program (with students driving): implement it
  * Need a weighted digraph class
  * We can use `heapq` as a priority queue:
    * https://docs.python.org/3/library/heapq.html
    * Use an empty list to start a queue
    * Use functions in this library to manipulate it
    * Generally push (priority, object) pairs
    * This doesn't easily support altering priorities
      * What solution is offered in the documentation?
      * How could we do better (simpler) if we knew that priorities were only being *reduced*?