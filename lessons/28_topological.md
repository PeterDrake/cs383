**Bring Cormen**

# Topological sorting
* Problem (CLSR 574)
  * This must be a dag or it's unsolvable!
* Simple algorithm:
  * Run DFS starting from each vertex
  * As each vertex is finished (i.e., after all neighbors are processed), add it to front of result
    * TPS: Should the result be stored as an array-based or linked list, and why?
    * Equivalently, add it to end and reverse result when done
* Why does this work?
  * At the time a vertex is finished, everything downstream of it must also be finished
* Time is same as DFS: $V + E$
* Students: implement it

