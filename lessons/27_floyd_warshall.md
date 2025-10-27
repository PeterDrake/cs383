# Floyd-Warshall Algorithm
* All-pairs shortest paths in a potentially weighted graph
* Incremental algorithm
  * Set up a distances-to matrix with everything initialized to infinity
  * Set distances along edges to edge weights, distance from each edge to itself to 0
  * Now the distances are correct under the tight constraint that no intermediate vertices are allowed
  * For each vertex `i`
    * For each pair of vertices `v`, `w`
      * If distances `v` … `i` + `i` … `w` < `v` … `w`, reduce distance `v` … `w`
      * Now distance is correct allowing vertices 0 through `i` as intermediate
* This is an example of a *dynamic programming* algorithm, where you use stored solutions to easier problems to solve harder problems
  * This is the bottom-up version of what recursion does top-down
  * Recursion can get expensive if you have to recompute values, but you can avoid this by memoization
* Students: implement it!
* Analysis
  * Is this better than just running Dijkstra from each vertex?
* Variant: detect negative cycles
  * What would be true (in the result matrix) after an update if there were a negative cycle?
  * Stop as soon as this happens.
* Variant: also compute edge-to for each path
