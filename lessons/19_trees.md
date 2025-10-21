# Trees
* Motivation
  * Directory structures, genetic trees, structure of code (libraries and subclasses), search trees
* Terminology
  * On a sample binary tree with letters, identify:
    * Root
    * Leaves (include some red herrings with one child)
    * Internal nodes
    * Parent
    * Children
    * Sibling
    * Ancestors
    * Descendants
    * Depth
    * Height
  * TPS:
    * For height $h$, $h + 1 <= n <= 2^{h+1} - 1$
    * For $n$ nodes, $\lceil log_2(n+1) -1 \rceil <= h <= n - 1$
      * $\lceil log_2(n+1) -1 \rceil = \lfloor{log_2(n)}\rfloor$; the latter is simpler but doesn't work if if $n = 0$
  * Takeaway: $n \in O(2^h)$, $h \in \Omega(log n)$
* Implementation as nodes (mob program)
  * Internal `Node` class within `BinaryTree` class
* Traversals (ideas)
  * Pre, in, post, level
  * Can be used as search (DFS vs BFS)
* Mob program
  * Level order with explicit queue
  * Preorder with explicit stack (or wave hands at it if short on time)
  * Preorder with recursion
  * Inorder
