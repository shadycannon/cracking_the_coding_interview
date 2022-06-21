#!/usr/bin/python3
from collections import deque


class BinaryTree:
    def __init__(self):
        self.root = None


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def add_left_leaf(tree, value):
    node = tree.root
    while node.left:
        node = node.left
    node.left = Node(value)

def add_right_leaf(tree, value):
    node = tree.root
    while node.right:
        node = node.right
    node.right = Node(value)


def build_balanced_binary_tree(values: list,) -> BinaryTree:
    bt = BinaryTree()
    bt.root = Node(values[0])
    q = deque()
    q.append(bt.root)
    i = 1
    for i in range(1, len(values)):
        node = q.popleft()
        node.left = Node(values[i])
        if i+1 < len(values):
            node.rigth = Node(values[i+1])











def problem1():
    """Implement a function to check if a binary tree is balance.
    For the purposes of this question, a balanced tree is defined
    to be a tree such that the hieghts of the two subtrees of any
    node never differ by more than one"""

if __name__ == "__main__":
    values = [1, 2, 4, 5, 3]