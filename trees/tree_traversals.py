# Node Structure
class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=", ")
        inorder(root.right)

def preorder(root):
    if root:
        print(root.data, end=", ")
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=", ")

def levelorder(root):
    if not root:
        return
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.data, end=", ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


# Example Tree
root = Node(1)
root.left, root.right = Node(2), Node(3) 
root.left.left, root.left.right = Node(4), Node(5)
root.right.left, root.right.right = Node(6), Node(7)


print("Inorder: ")
inorder(root)
print("\nPreorder: ")
preorder(root)
print("\nPostorder: ")
postorder(root)
print("\nLevelorder: ")
levelorder(root)
print("\n")
