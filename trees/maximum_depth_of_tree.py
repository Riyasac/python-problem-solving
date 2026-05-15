"""
Maximum Depth or Height of a Binary Tree

Given the root of a binary tree, find the maximum depth of the tree. The maximum depth or height of the tree is the number of edges in the tree from the root to the deepest node.

Example 1

Input:
    12
    / \
   8  18
  / \
 5  11

Output: 2

Explanation: The longest path from the root node to deepest node has 2 edges.
______________________________________________________________________________________

Example 2

Input:
    1
   / \
  2   3
 /   / \
4   10  5
       / \
      6   7

Output: 3

Explanation: The longest path from the root (node 1) to deepest leaf (node 6) has 3 edges.

"""

class TreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def max_depth(root):
    if not root:
        return -1  # return -1 so that leaf node has height 0 (edges count)

    return 1 + max(max_depth(root.left), max_depth(root.right))


if __name__ == "__main__":

    # Initialize Tree
    #       12
    #      / \
    #     8   18
    #    / \
    #   5   11
    
    root = TreeNode(12)
    root.left = TreeNode(8, TreeNode(5), TreeNode(11))
    root.right = TreeNode(18)

    depth = max_depth(root)
    print(f"Maximum depth of binary tree is {depth}")

    # Initialize Tree
    #       1
    #      / \
    #     2   3
    #    /   / \
    #   4   10  5
    #          / \
    #         6   7
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.right = TreeNode(3, None, TreeNode(5, TreeNode(6), TreeNode(7)))

    depth = max_depth(root)
    print(f"Maximum depth of binary tree is {depth}")
