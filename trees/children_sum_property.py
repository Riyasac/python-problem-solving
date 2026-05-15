"""
Check for Children Sum Property in a Binary Tree

Given a binary tree, the task is to check for every node, its value is equal to the sum of values of its immediate left and right child. For NULL values, consider the value to be 0. Also, leaves are considered to follow the property.
Input:
"""
#      10
#     /  \
#    8    2
#   /\   /
#  3  5 2

# Output: 1
# Explanation: The above binary tree follows the Children Sum Property.
# ___________________________________________________________________________
# Input:
#      10
#     /  \
#    8    2
#   /\   /
#  2  5 2

# Output: 0
# Explanation: The above binary tree doesn't follows the Children Sum Property as 5 + 2 != 8

class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def is_sum_property(root):
    if root is None or (root.left is None and root.right is None):
        return 1

    left = root.left.data if root.left else 0
    right = root.right.data if root.right else 0
    if (
        root.data == (left + right) and 
        is_sum_property(root.left) and 
        is_sum_property(root.right)
    ):
        return 1
    else:
        return 0
    

if __name__ == "__main__":
    root = TreeNode(10, TreeNode(8, TreeNode(2), TreeNode(5)), TreeNode(2, TreeNode(2)))
    print(is_sum_property(root))
