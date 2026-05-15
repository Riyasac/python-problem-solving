"""
Balanced Binary Tree or Not

Given the root of a binary tree, determine if it is height-balanced. A binary tree is considered height-balanced if the absolute difference in heights of the left and right subtrees is at most 1 for every node in the tree.

Examples:

Input:
    10
   /  \
  20  30
 /  \
40  60

Output: true
Explanation: The height difference between the left and right subtrees at all nodes is at most 1. Hence, the tree is balanced.  

"""
class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def depth(node):
    if node is None:
        return 0

    return 1 + max(depth(node.left), depth(node.right))


def is_balanced(root):
    if root is None:
        return True

    # Get the depth of left and right sub trees
    left_depth = depth(root.left)
    right_depth = depth(root.right)

    if abs(left_depth - right_depth) > 1:
        return False

    # Recursively check the left and right subtrees
    return is_balanced(root.left) and is_balanced(root.right)

if __name__ == "__main__":
    root = TreeNode(10, TreeNode(20, TreeNode(40), TreeNode(60)), TreeNode(30))
    balanced = is_balanced(root)
    print("Tree is balanced" if balanced else "Tree is not balanced")
    
    root = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(5))), TreeNode(3))
    balanced = is_balanced(root)
    print("Tree is balanced" if balanced else "Tree is not balanced")
