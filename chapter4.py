#!/usr/bin/python3
from collections import deque, defaultdict
import math
from typing import Dict, Generator, List, Optional, Tuple

from chapter2 import LinkedList, Node

class BinaryTree:
    def __init__(self):
        self.root = None

    def visualize_tree(self) -> None:
        bt = self
        _, height = traverse_tree_and_print_height(direction_graph.root)
        node = bt.root
        q = deque()
        q.append((node, 0))
        output_data = defaultdict(list)

        while q:
            node, level = q.popleft()
            buffer_length = math.pow(2, (height - 1 - level)) - 1
            pre_buffer = int(buffer_length) * ' '
            post_buffer = (int(buffer_length) + 1) * ' '
            if not node:
                output_data[level].append(f'{pre_buffer} {post_buffer}')
                level += 1
                continue
            output_data[level].append(f'{pre_buffer}{node.data}{post_buffer}')
            level += 1

            if node.left:
                q.append((node.left, level))
            else:
                q.append((None, level))
            if node.right:
                q.append((node.right, level))
            else:
                q.append((None, level))

        for i in range(0, len(output_data)):
            print(''.join(output_data[i]))

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None


def add_left_leaf(tree, value):
    node = tree.root
    while node.left:
        node = node.left
    node.left = TreeNode(value)


def add_right_leaf(tree, value):
    node = tree.root
    while node.right:
        node = node.right
    node.right = TreeNode(value)


def build_balanced_binary_tree(values: List[int]) -> BinaryTree:
    bt = BinaryTree()
    bt.root = TreeNode(values[0])
    q = deque()
    q.append(bt.root)
    for i in range(1, len(values), 2):
        node = q.popleft()
        node.left = TreeNode(values[i])
        q.append(node.left)
        if i + 1 < len(values):
            node.right = TreeNode(values[i + 1])
            q.append(node.right)
    return bt


def traverse_tree_and_print_height(root: TreeNode, height: int = 0) -> Tuple[bool, int]:
    if not root:
        return True, height

    balanced_left, left_height = traverse_tree_and_print_height(root.left, height + 1)
    balanced_right, right_height = traverse_tree_and_print_height(root.right, height+1)
    if not balanced_right or not balanced_left:
        return False, left_height
    bigger_height = max(left_height, right_height)
    if abs(left_height - right_height) > 1:
        return False, bigger_height
    return True, bigger_height


def build_unbalanced_tree(values: List[int]) -> BinaryTree:
    bt = BinaryTree()
    bt.root = TreeNode(values[0])
    q = deque()
    q.append(bt.root)
    for i in range(1, len(values)):
        node = q.popleft()
        node.left = TreeNode(values[i])
        q.append(node.left)

    return bt


def find_node(root, data) -> True:
    if not root:
        return None
    if root.data == data:
        return root

    node_found_left = find_node(root.left, data)
    if node_found_left:
        return node_found_left
    return find_node(root.right, data)


def split_up_lists(values: List[int]) -> Tuple[TreeNode, List[int], List[int]]:
    mid_point = int(len(values)/2)
    root_value = values[mid_point]
    root = TreeNode(root_value)
    left_values = values[0:mid_point]
    right_values = values[mid_point+1:]
    return root, left_values, right_values


def construct_binary_search_tree(root: TreeNode, left_values: List[int], right_values: List[int]) -> None:
    if len(left_values) == 1:
        root.left = TreeNode(left_values[0])
    elif left_values:
        root.left, sub_left_values, sub_right_values = split_up_lists(left_values)
        construct_binary_search_tree(root.left, sub_left_values, sub_right_values)

    if len(right_values) == 1:
        root.right = TreeNode(right_values[0])
    elif right_values:
        root.right, sub_left_values, sub_right_values = split_up_lists(right_values)
        construct_binary_search_tree(root.right, sub_left_values, sub_right_values)


def traverse_and_track_depth(root: TreeNode, level: int, lls: Dict[int, LinkedList], curs: Dict[int, Node]) -> List[LinkedList]:
    if not root:
        return
    print(root.data)

    current = curs.get(level, None)

    if not lls.get(level, None):
        lls[level] = LinkedList()
        lls[level].headval = Node(root.data)
        current = lls[level].headval
    else:
        current.next = Node(root.data)
        current = current.next
    curs[level] = current
    traverse_and_track_depth(root.left, level + 1, lls, curs)
    traverse_and_track_depth(root.right, level + 1, lls, curs)


def determine_if_bst(root: TreeNode) -> bool:
    if not root:
        return True
    if root.left and root.left.data > root.data:
        print(f'left ({root.left.data}) is bigger than root ({root.data})')
        return False

    if root.right and root.right.data < root.data:
        print(f'right ({root.right.data}) is bigger than root ({root.data})')

        return False
    return determine_if_bst(root.left) and determine_if_bst(root.right)


def in_order_traversal(root: TreeNode) -> None:
    if not root:
        return
    in_order_traversal(root.left)
    print(root.data)
    in_order_traversal(root.right)


def add_parents_to_tree(root: TreeNode) -> None:
    if not root:
        return
    if root.left:
        root.left.parent = root
    if root.right:
        root.right.parent = root
    add_parents_to_tree(root.left)
    add_parents_to_tree(root.right)


def is_left(node: TreeNode) -> bool:
    parent = node.parent
    if parent:
        if node is parent.left:
            return True
    return False


def is_right(node: TreeNode) -> bool:
    parent = node.parent
    if parent:
        if node is parent.right:
            return True
    return False


def find_leftmost_leaf(node: TreeNode) -> TreeNode:
    if not node.left:
        return node
    return find_leftmost_leaf(node.left)


def find_first_parent_of_left(node: TreeNode) -> TreeNode:
    if not node:
        return None
    if is_left(node):
        return node.parent
    return find_first_parent_of_left(node.parent)


def find_ancestors(root: TreeNode, node1: TreeNode, node2: TreeNode) -> Optional[TreeNode]:
    if not root:
        return None
    if is_node_in_tree(root, node1) and is_node_in_tree(root, node2):
        left_found = find_ancestors(root.left, node1, node2)
        right_found = find_ancestors(root.right, node1, node2)
        if left_found:
            return left_found
        if right_found:
            return right_found
        else:
            return root
    return None


def is_node_in_tree(root: TreeNode, node: TreeNode) -> bool:
    if not root:
        return False
    if root is node:
        return True
    return is_node_in_tree(root.left, node) or is_node_in_tree(root.right, node)


def traverse_simultaneously(small_root: TreeNode, large_root: TreeNode) -> bool:
    if not small_root:
        return True
    if not large_root:
        return False

    if small_root.data != large_root.data:
        return False
    left_equal = traverse_simultaneously(small_root.left, large_root.left)
    right_equal = traverse_simultaneously(small_root.right, large_root.right)
    return left_equal and right_equal


def find_matching_root(large_root: TreeNode, small_root_data: int) -> Generator[TreeNode, None, None]:
    q = deque()
    q.append(large_root)
    while q:
        node = q.popleft()
        if node.data == small_root_data:
            yield node
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    yield None


def find_sums_from_root(root: TreeNode, value: int, paths:  List[str], path: List[int]) -> None:
    if not root:
        return
    new_path = path[:]  # copy list so pass by reference doesn't mess with things
    path = new_path
    path.append(root.data)
    current_sum = sum(path)
    if current_sum == value:
        paths.append(','.join([str(x) for x in path]))
        return
    if current_sum > value:
        return  # recursing further will only create larger values
    new_path = path[:]
    find_sums_from_root(root.left, value, paths, new_path)
    find_sums_from_root(root.right, value, paths, path)


def find_all_sums(root: TreeNode, value: int, paths: List[str]) -> None:
    if not root:
        return
    find_sums_from_root(root, value, paths, [])
    find_all_sums(root.left, value, paths)
    find_all_sums(root.right, value, paths)


def problem1(bt: BinaryTree) -> bool:
    """Implement a function to check if a binary tree is balance.
    For the purposes of this question, a balanced tree is defined
    to be a tree such that the heights of the two subtrees of any
    node never differ by more than one"""
    balanced, height = traverse_tree_and_print_height(bt.root)
    return balanced


def problem2(root: TreeNode, starting_city: str, ending_city: str) -> bool:
    """Given a directed graph, design an algorithm to find out whether
    there is a route between two nodes"""
    pass
    # depth first traversal
    starting_node = find_node(root, starting_city)
    if not starting_node:
        return False
    ending_node = (starting_node, ending_city)
    if not ending_node:
        return False
    return True


def problem3(values: List[int]) -> BinaryTree:
    """Given a sorted array with unique integer elements, write an algorithm to
    create a binary search tree with minimal height"""
    bt = BinaryTree()
    bt.root, left_values, right_values = split_up_lists(values)
    construct_binary_search_tree(bt.root, left_values, right_values)
    return bt


def problem4(bt: BinaryTree):
    """Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth"""
    lls = dict()
    traverse_and_track_depth(bt.root, 0, lls, dict())
    for ll in lls.values():
        ll.print()


def problem5(bt: BinaryTree) -> bool:
    """Implement a function to check if a binary tree is a bst"""
    return determine_if_bst(bt.root)


def problem6(bt: BinaryTree, node: TreeNode) -> TreeNode:
    """Write an algorithm to find the 'next' (in order) node of a given node in a
     binary search tree. You may assume each node has a link to its parent"""
    add_parents_to_tree(bt.root)
    if node.right:
        return find_leftmost_leaf(node.right)
    if is_left(node):
        return node.parent
    if is_right(node):
        return find_first_parent_of_left(node)


def problem7(bt: BinaryTree, node1: TreeNode, node2: TreeNode) -> TreeNode:
    """Design an algorithm and write code to find the first common ancestor of two nodes in a
    binary tree. Avoid storing additional nodes in a data struture"""
    return find_ancestors(bt.root, node1, node2)

def problem8(large_bt: BinaryTree, small_bt: BinaryTree) -> bool:
    """You have two very large binary trees. T1, with millions of nodes and T2, with hundreds of nodes.
    Create an algorithm to decide if T2 is a subtree of T1"""
    # breadth first T1 until finding a matching root node
    # traverse T2 and T1 simultaneously
    for starting_root in find_matching_root(large_bt.root, small_bt.root.data):
        if traverse_simultaneously(starting_root, small_bt.root):
            return True
    return False


def problem9(bt: BinaryTree, value: int) -> List[str]:
    """You are given a binary tree in which each node contains a value.
    Design an algorithm to print all paths which sum to a given value. The path
    does not need to start at a node or a root"""
    path_list = []
    find_all_sums(bt.root, value, path_list)
    return path_list


if __name__ == "__main__":
    # problem 1
    balanced_tree = build_balanced_binary_tree([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5])
    unbalanced_tree = build_unbalanced_tree([0, 1, 2, 3, 4])
    print(problem1(balanced_tree))
    print(problem1(unbalanced_tree))

    # problem 2
    direction_graph = build_balanced_binary_tree(['San Francisco', 'Oakland', 'Austin', 'Seattle', 'San Diego', 'Honolulu', 'New York', 'St. Louis', 'LA'])
    print(problem2(direction_graph.root, 'San Francisco', 'LA'))
    print(problem2(direction_graph.root, 'Seattle', 'LA'))
    print(problem2(direction_graph.root, 'San Diego', 'LA'))

    # problem 3
    binary_search_tree = problem3([1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15])
    binary_search_tree.visualize_tree()

    # problem 4
    print(problem4(binary_search_tree))

    # problem 5
    false_binary_search_tree = problem3([1, 3, 19, 6, 7, 8, 10, 13, 14])
    print(problem5(binary_search_tree))
    print(problem5(false_binary_search_tree))

    # problem 6
    add_parents_to_tree(binary_search_tree.root)
    node = binary_search_tree.root.left.left.left
    while node:
        next = problem6(binary_search_tree, node)
        node = next

    # problem 7
    binary_search_tree.visualize_tree()
    node = problem7(binary_search_tree, binary_search_tree.root.left.left.left, binary_search_tree.root.left.left.right)

    # problem 8
    small_tree = BinaryTree()
    tn1 = TreeNode(5)
    tn2 = TreeNode(3)
    tn3 = TreeNode(7)
    tn4 = TreeNode(6)
    small_tree.root = tn1
    tn1.left = tn2
    tn1.right = tn3
    tn3.left = tn4
    small_tree.visualize_tree()
    print(problem8(binary_search_tree, small_tree))

    # problem 9
    print(problem9(binary_search_tree, 21))