**Bring Cormen**

# Kosaraju-Sharir (strongly connected components)
* Diagram on p. 577 of Cormen
  * What is a strongly connected component?
  * Motivation: first paragraph of Cormen 20.5
  * Component graph
    * TPS: Can we guarantee that the component graph is acyclic?
  * Transposing a directed graph (has same strongly connected components)
* The algorithm:
  * DFS (starting from each vertex), adding each finished vertex to a list
  * Compute transpose of graph
  * DFS on the transposed graph, again from each vertex but going through the list from above in reverse order
    * Each tree in this DFS is a SCC
* This is a "transform" algorithm, because it reduces the SCC problem to DFS
* Class: carry out the algorithm by hand
* Why does this work?
  * Whatever SCC you start in, you will have explored all of it by the time you finish
  * The first DFS topologically sorts the component graph
  * The vertex $v$ that was finished last in the first DFS is visited first in the second DFS
  * There are no edges into that SCC in the original graph, and therefore no edge out of it in the transposed graph
  * A search from $v$ therefore finds exactly $v$'s SCC
  * The next vertex searched (because we skip over those in $v$'s SCC) will be in an SCC that, in the original graph, has no edges coming in except possibly from $v$'s SCC
  * That vertex will therefore find another SCC, and so on.
* Running time: $V + E$, because it's two DFSs
* If time, implement it
