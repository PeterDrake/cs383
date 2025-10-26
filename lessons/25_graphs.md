# Graphs
* Terminology
  * Vertex (plural is vertices) (aka node)
  * Edge
    * Analysis usually in terms of $V$ and $E$
  * Directed vs undirected
  * Weighted
  * Self-loop, parallel edge
  * Path
  * Cycle
  * Connected
    * Be careful with directed graphs
  * Dense vs sparse
  * Tree: acyclic connected graph
  * DAG: directed acyclic graph
  * TPS: In a connected, undirected graph with $V$ vertices, what is the minimum and maximum number of edges?
* Representation
  * Adjacency (neighbor) matrix
  * Adjacency lists
  * Analysis
  * Lists are usually better because most graphs are sparse
  * [graph.py](../src/graph.py)
  * [digraph.py](../src/digraph.py)
* DFS
  * Good for “can you get there from here”
  * Have to keep track of already-visited vertices
  * May have to try starting from each vertex in case of an unconnected graph
  * General technique: class for each algorithm, where constructor does the work
    * [dfs.py](../src/dfs.py)
* BFS
  * Good for finding shortest paths
  * Uses a queue in place of an implicit stack
  * [bfs.py](../src/bfs.py)