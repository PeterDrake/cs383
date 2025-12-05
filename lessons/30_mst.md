**Bring Cormen**

# Minimum spanning trees
* Diagram from Cormen, p. 586 (initially without weights)
* Definition of a spanning tree
  * Graph must be connected for such a tree to exist
* (add weights)
* Definition of minimum spanning tree
  * TPS: Can there ever be more than one correct answer?
* Applications: circuit design, computers, transit systems

# General incremental algorithm
* Idea
  * Start with no edges
  * Repeatedly add "safe" edges until you have a MST
    * (safe means that you always have a subset of the edges in the MST)
* The cheapest edge that connects two pieces not already connected must be in the MST
  * Otherwise, adding this cheap edge at the end would form a cycle, and removing some other edge in that cycle would create a cheaper MST

## Kruskal's algorithm:
* Always choose the cheapest edge that connects two unconnected components
* How to keep track of the connected components? Disjoint set forest!
* Idea
  * Sort the edges by weight
  * For each one, if its endpoints aren't connected:
    * Add that edge to the result
    * Merge the sets containing the endpoints
* Walk through example
* Analysis:
  * $O(V)$ to create the individual sets
  * $O(E \log E)$ to sort the edges
  * $E$ passes through loop, each of which performs a couple of disjoint set operations, totalling $O(E \log V)$
  * Since $\log E \in O(\log V)$ because $E \leq V^2$, this adds up to $O(E \log V)$
* TPS: Could you stop early?

## Prim's algorithm:
* Start with one vertex, then find the cheapest edge connecting the growing tree to a new vertex
* How to keep track of the cheapest edge? Index min priority queue, where the priority is the cost of the cheapest edge from the tree (initially infinity)
* Idea
  * Set every vertex's parent to None
  * Set root's priority to 0, others to infinity
  * Create a priority queue with the root at position 0, the rest in arbitrary order after
  * While the queue is not empty
    * Dequeue to get `v`
    * For each neighbor `w` of `v`:
      * If `w` is in the queue and `weight(v, w)` < `w`'s current priority
        * Set `w`'s parent to `v`
        * Reduce `w`'s priority
* Walk through example
* Analysis:
  * $O(V)$ to initialize
  * $O(V \log V)$ dequeueings
  * $O(E \log V)$ priority reductions
  * Adds up to $O(E \log V) = O(E \log E)$ for a connected graph
    * This can be improved using a Fibonacci heap
* TPS: Could you stop early?
* S&W: "Kruskal's algorithm is generally slower than Prim's"
