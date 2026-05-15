"""
Sorted Array to Balanced BST

Given a sorted array arr[]. Convert it into a Balanced Binary Search Tree (BST). Return the root of the BST.

A Balanced Binary Search Tree (BST) is a type of binary tree in which the difference between the heights of the left and right subtrees of every node is at most one.

Examples: 

    Input: arr[] = [10, 20, 30]
    Output: [[20], [10, 30]]
    Explanation: The above sorted array converted to below Balanced Binary Search Tree.
    
Input:
    20
   /  \
  10  30
____________________________________________________________________________________________

Input:  arr[] = [1, 5, 9, 14, 23, 27]
Output: [[9], [1, 23], [N, 5, 14, 27]]
Explanation: The above sorted array converted to below Balanced Binary Search Tree.
        9
       / \
      1   23
      \   / \
       5 14  27
           
"""
from collections import deque


# Node structure
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# function to get height
def getHeight(root, h):
    if root is None:
        return h - 1
    return max(getHeight(root.left, h + 1), getHeight(root.right, h + 1))


# Print level order
def levelOrder(root):
    queue = deque([[root, 0]])
    lastLevel = 0

    # function to get the height of tree
    height = getHeight(root, 0)

    # printing the level order of tree
    while queue:
        node, lvl = queue.popleft()

        if lvl > lastLevel:
            print()
            lastLevel = lvl

        # all levels are printed
        if lvl > height:
            break

        # printing null node
        print("N" if node.data == -1 else node.data, end=" ")

        # null node has no children
        if node.data == -1:
            continue

        if node.left is None:
            queue.append([Node(-1), lvl + 1])
        else:
            queue.append([node.left, lvl + 1])

        if node.right is None:
            queue.append([Node(-1), lvl + 1])
        else:
            queue.append([node.right, lvl + 1])


# Recursive Function to Create BST
def sortedArrayToBSTRecur(arr, start, end):
    if start > end:
        return None

    mid = start + (end - start) // 2
    root = Node(arr[mid])

    # Divide from middle element
    root.left = sortedArrayToBSTRecur(arr, start, mid - 1)
    root.right = sortedArrayToBSTRecur(arr, mid + 1, end)

    return root


# Function which return BST
def sortedArrayToBST(arr):
    return sortedArrayToBSTRecur(arr, 0, len(arr) - 1)


if __name__ == "__main__":

    arr = [10, 20, 30]
    root = sortedArrayToBST(arr)
    levelOrder(root)
    print("\n")

    arr = [1, 5, 9, 14, 23, 27]
    root = sortedArrayToBST(arr)
    levelOrder(root)
