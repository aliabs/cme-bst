# This is a sample Python script.

import sys

MAX = sys.maxsize
MIN = -sys.maxsize - 1


class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


# Returns true if tree is BST
def is_bst(node, min_=MIN, max_=MAX):
    if node is None:
        return True
    if node.data < min_ or node.data > max_:
        return False
    return (is_bst(node.left, min_, node.data - 1) and
            is_bst(node.right, node.data + 1, max_))


if __name__ == '__main__':
    root = Node(6)
    root.left = Node(2)
    root.right = Node(7)
    root.left.left = Node(1)
    root.left.right = Node(3)
    if is_bst(root):
        print("is BST!")
    else:
        print("Not BST!")
