class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


if __name__ == "__main__":
    node1 = Node("A")     
    node2 = Node("B")     
    node3 = Node("C")
    node4 = Node("D")

    node1.next_node = node2     
    node2.next_node = node3
    node3.next_node = node4

    current_node = node1

    print("Linked List Traversal:")
    while current_node is not None:
        print(current_node.data, end="->")
        current_node = current_node.next_node
    print("\n")