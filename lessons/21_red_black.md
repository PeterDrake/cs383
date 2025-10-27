**Bring Sedgewick & Wayne**

# Red-black trees
* Goal: logarithmic worst-case performance for a set/dictionary implementation
* Invariant
  * Binary search tree
  * Example: (((5) B10) B15 (B20))
  * Each link is red or black
    * For convenience, links to null are black
    * In implementation, node is color of link from parent
  * The root (if any) is black
  * No node has two red links connected to it (up or down)
  * Every path from the root to null has the same number of black links
  * Red links lean left
    * Some sources don't include this, but it makes code simpler

## Analysis
* Consider the shortest path to a leaf. The tree including that level and above is perfect and contains $n$ nodes or fewer. The length of the longest path within this part of the tree has length no more than $\lg n$. No path in the full tree has a path more than twice this long. The worst case is therefore $O(\log n)$. The longest path can't have length less than $\lg n$ (as it would in a complete tree), so the worst case is also $\Omega(\log n)$ and therefore $\Theta(\log n)$. 

## Search
* Identical to BST

## Insertion
* Idea: add a red child normally, then fix the tree
* Tools for fixing the tree:
  * Color changes
  * Rotations
    * In keeping colors of moving links, rotation changes colors of nodes
    * Simple example: insert 22 in tree above, then rotate left to get (((5) B10) B15 ((20) B22))
    * If there is a middle subtree, it swings across
* Repair starts with parent of inserted node and works up the tree backing out of the recursion
* Possible problems when a new red node appears in the tree (see S&W 438)
  * New node is root
    * Red root problem
  * New node is a right child
    * This handled differently depending on color of sibling
      * L black, R red problem
      * L red, R red problem
  * New node is left child
    * Only a problem if parent is red
      * L red, LL red problem
* [red_black.py](../src/red_black.py) (falling through ifs!)
  * L black, R red: rotate left
    * May cause L red, LL red problem on next level up
  * L red, LL red: rotate right
    * Causes L red, R red problem
  * L red, R red: flip colors of node and both children
    * Introduces red node at next level up
  * At end of recursion, color root black (red root problem)
  * Do examples (insert random integers in [1, 100])

## Deletion
* Too complicated, but same idea
