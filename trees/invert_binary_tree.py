"""
Invert Binary Tree - Change to Mirror Tree

Given the root of binary tree, Convert it into its mirror. A mirror of a binary tree is another tree in which the left and right children of every non-leaf node are interchanged.

Example 1:

Input:
     1
    / \
   2   3
  / \
 4   5

Output:
     1
    / \
   3   2
      / \
     5   4

Explanation: In the inverted tree, every non-leaf node has its left and right child interchanged.
"""

def invert_tree(root):
    if root is None:
        return root
    
    # Swap left and right children
    root.left, root.right = root.right, root.left     

    # Recursively invert subtrees
    invert_tree(root.left)
    invert_tree(root.right)
    return root


def preorder(root):
    if root:
        print(root.data, end=", ")
        preorder(root.left)
        preorder(root.right)


class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


if __name__ == "__main__":

    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))

    print("Preorder before inversion:")
    preorder(root)

    inverted_tree = invert_tree(root)
    print("\nPreorder after inversion:")
    preorder(inverted_tree)
    print("\n")
