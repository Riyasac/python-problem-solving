"""
Symmetric Tree

Given the root of a binary tree, determine whether it is symmetric around root, i.e., check if the binary tree is a mirror image of itself.

Example 1:

Input:
    10
    / \
   5   5
  /     \
 2       2

Output: true
Explanation: Tree is mirror image of itself i.e. tree is symmetric.

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

def symmetric_tree(root) -> bool:
    if root is None:
        return True
    
    return is_mirror(root.left, root.right)

def is_mirror(left_sub, right_sub):
    if left_sub is None and right_sub is None:
        return True

    # One of them is null, so they aren't mirror images
    if left_sub is None or right_sub is None or left_sub.data != right_sub.data:
        return False

    # Check if the subtrees are mirrors
    return (
        is_mirror(left_sub.left, right_sub.right) and
        is_mirror(left_sub.right, right_sub.left)
    )

if __name__ == "__main__":
    
    root = TreeNode(10, TreeNode(5, TreeNode(2)), TreeNode(5, None, TreeNode(2)))
    symmetric = symmetric_tree(root)
    print("Tree is symmetric" if symmetric else "Tree is not symmetric")
