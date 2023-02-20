class Node:
    def __init__(self, value):
        self.value = value
        self.next = None # Type: Node

    def traverse(self, head) -> None:
        currentNode = head
        while currentNode:
            print(currentNode.val)
            currentNode = currentNode.next