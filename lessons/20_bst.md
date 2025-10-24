# Binary search trees
* Definition
  * Binary tree where left subtree < root < right subtree
    * Emphasize notion of invariant
  * Ineorder traversal of a BST is increasing order
* Algorithm ideas
  * Search
  * Insertion
  * Deletion
* Random students do examples of insertion and deletion

## Implementation
* [bst.py](../src/bst.py)
  * `contains`
  * `add`
    * Note that recursive helper method returns the improved subtree
  * `_remove_min`
  * `_min_node`
  * `remove`
    * Tricky reference operations -- have students draw pictures at each point

## Analysis
  * `contains`, `add`, and `remove` take time proportional to tree height
  * Best and average case: logarithmic
  * Worst case: linear

## Comparison to hash table
  * Worse on average, same in worst case
      * But worst case is much more likely for BST
  * Keys must be comparable
  * Can do things like min, max, range search, rank, traverse in order
  * Foreshadow red-black trees
