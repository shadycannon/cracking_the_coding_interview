#!/usr/bin/python3

from typing import Tuple


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.headval = None


def problem1(ll: LinkedList) -> LinkedList:
    """Write code to remove duplicates from a Linkedlist
    FOLLOW UP
    How would you solve this problem if a temporary buffer is not allowed?
    """
    # buffer = []
    # node = ll.headval
    # prev = None
    # while node:
    #     data = node.data
    #     if data in buffer:
    #         prev.next = node.next
    #    else:
    #         buffer.append(data)
    #     prev = node
    #     node = node.next

    # return ll

    current = ll.headval
    while current:
        data = current.data
        print(data)
        runner = current
        while runner:
            if runner.next and data == runner.next.data:
                runner.next = runner.next.next
            runner = runner.next
        current = current.next

    return ll


def problem2(ll: LinkedList, k: int) -> Node:
    """Implement an algorithm to find the kth to last element of a singly Linked List"""
    runner = ll.headval
    current = ll.headval

    for _ in range(k):
        runner = runner.next
    while runner:
        current = current.next
        runner = runner.next
    return current


def problem3(n: Node) -> None:
    """Implement an algorithm to delete a node in the middle of a singly linked list,
    given access only to that node"""
    if not n.next:
        return
    next = n.next
    n.data = next.data
    n.next = next.next


def problem4(ll: LinkedList, x: int) -> LinkedList:
    """Write code to partition a linked list around a value x, such that all nodes less than x
    come before all nodes greater than or equal to x"""
    list_before = LinkedList()
    list_after = LinkedList()
    node_before = None
    node_after = None
    node = ll.headval
    while node:
        data = node.data
        if data < x:
            if not node_before:
                list_before.headval = Node(data)
                node_before = list_before.headval
            else:
                node_before.next = Node(data)
                node_before = node_before.next
        else:
            if not node_after:
                list_after.headval = Node(data)
                node_after = list_after.headval
            else:
                node_after.next = Node(data)
                node_after = node_after.next
        node = node.next

    node_before.next = list_after.headval
    print_ll(list_before)
    return list_before


def turnLinkedListToAnInt(ll: LinkedList) -> int:
    current = ll.headval
    number = 0
    tens_value = 0
    while current:
        data = current.data
        print(f'd: {data}')
        number += (10 ** tens_value) * data
        current = current.next
        tens_value += 1
    return number


def problem5(ll1: LinkedList, ll2: LinkedList) -> LinkedList:
    """You have two numbers represented by a linked list, where each node contains a single digit.
    The digits are store in reverse order, such that the 1's digit is aat the head of the list.
     Write a function that adds the two numbers and returns the sum as a linked list
     e.g. (7 -> 1 -> 6) + (5 -> 9 -> 2) aka 617 + 295"""
    node1 = ll1.headval
    node2 = ll2.headval
    sumll = LinkedList()
    carry_over = 0
    sum_pointer = None
    while node1 or node2:
        if node1:
            data1 = node1.data
            node1 = node1.next
        else:
            data1 = 0

        if node2:
            data2 = node2.data
            node2 = node2.next

        else:
           data2 = 0
        sum = data1 + data2 + carry_over
        if sum < 10:
            digit = sum
            carry_over = 0
        else:
            digit = sum - 10
            carry_over = 1

        if not sum_pointer:
            sumll.headval = Node(digit)
            sum_pointer = sumll.headval
        else:
            sum_pointer.next = Node(digit)
            sum_pointer = sum_pointer.next


    if carry_over == 1:
        sum_pointer.next = Node(1)

    return sumll


def problem6(ll: LinkedList) -> Node:
    """Given a circular linked list, implement an algorithm which returns
    the node at the beginning of the loop
    e.g. A -> B -> C -> D -> E -> C returns C"""
    slow_pointer = fast_pointer = ll.headval
    num_collisions = 0
    while slow_pointer:
        if slow_pointer == fast_pointer and slow_pointer != ll.headval:
            if not num_collisions:
                print(f"first collision!! {slow_pointer.data}")
                slow_pointer = ll.headval
                num_collisions += 1
            else:
                print("second collision!!")
                return slow_pointer

        slow_pointer = slow_pointer.next
        if num_collisions:
            fast_pointer = fast_pointer.next
        else:
            fast_pointer = fast_pointer.next.next


def recurse_palindrome(length: int, node: Node) -> Tuple[Node, bool]:
    print(f'n: {node.data} l: {length}')
    if not node or length == 0:
        return None, False
    if length == 1:
        print('ret true')
        return node.next, True

    comparison_node, comparison_result = recurse_palindrome(length - 2, node.next)
    print(f'n: {node.data}, cn: {comparison_node.data}, cr: {comparison_result}')
    if not comparison_result or not comparison_node:
        return comparison_node, comparison_result
    return comparison_node.next, node.data == comparison_node.data


def problem7(ll: LinkedList) -> bool:
    """Implement a function to check if a linked list is a palindrome"""
    length = 0
    node = ll.headval
    while node:
        length += 1
        node = node.next
    return recurse_palindrome(length, ll.headval)[1]


def print_ll(ll):
    node = ll.headval
    ret_str = ''
    while node:
        ret_str += f'{node.data} -> '
        node = node.next
    print(ret_str[:-4])


if __name__ == "__main__":
    ll = LinkedList()
    ll.headval = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(3)
    n6 = Node(2)
    n7 = Node(1)

    ll.headval.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7

    ll2 = LinkedList()
    ll2.headval = Node(7)
    l2n2 = Node(1)
    l2n3 = Node(6)

    ll2.headval.next = l2n2
    l2n2.next = l2n3

    ll1 = LinkedList()
    ll1.headval = Node(5)
    ll1n2 = Node(9)
    ll1.headval.next = ll1n2

    cll = LinkedList()
    cll.headval = Node(1)
    cn2 = Node(2)
    cn3 = Node(3)
    cn4 = Node(4)
    cn5 = Node(5)


    cll.headval.next = cn2
    cn2.next = cn3
    cn3.next = cn4
    cn4.next = cn5
    cn5.next = cn3


    print_ll(ll)
    print_ll(problem1(ll))
    print(problem2(ll, 4).data)
    problem3(n3)
    problem4(ll, 8)
    print(turnLinkedListToAnInt(ll1))
    print_ll(problem5(ll1, ll2))
    print(problem6(cll).data)
    print(problem7(ll))




