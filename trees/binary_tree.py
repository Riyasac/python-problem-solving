# Node Structure
class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


# Initialize
rootNode = Node(5)
secondNode = Node(4)
thirdNode = Node(8)
fourthNode = Node(1)

# Connect binary tree nodes
rootNode.left = secondNode
rootNode.right = thirdNode
secondNode.left = fourthNode


