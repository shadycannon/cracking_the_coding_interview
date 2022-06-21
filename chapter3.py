#!/usr/bin/python3
import sys

from datetime import datetime
from chapter2 import Node


class Stack:
    def __init__(self):
        self.top = None
        self.front = None

    def push(self, data):
        new_node = Node(data)
        if self.top:
            new_node.next = self.top
        else:
            self.front = new_node
        self.top = new_node

    def pop(self):
        if self.top:
            popped = self.top.data
            self.top = self.top.next
            return popped
        return None

    def peep(self):
        if self.top:
            return self.top.data

    def isEmpty(self):
        if not self.top:
            return True
        else:
            return False

    def popFront(self):
        node = self.top
        if not node.next:
            return self.pop()
        while node.next:
            next = node.next
            if not next.next:
                popped = next.data
                node.next = None
            else:
                node = next
        return popped

    def print_all(self, prepend):
        node = self.top
        s = ''
        while node:
            s += f'{node.data} -> '
            node = node.next
        print(f'{prepend} {s[:-4]}')


class StackWithMin(Stack):
    def __init__(self):
        super().__init__()
        self.internal_stack = Stack()

    def push(self, data):
        if data < self.min():
            self.internal_stack.push(data)
        return super().push(data)

    def pop(self):
        data = super().pop()
        if data == self.min():
            self.internal_stack.pop()
        return data

    def peek(self):
        return super().peep()

    def min(self):
        stack_min = self.internal_stack.peep()
        if not stack_min:
            return sys.maxsize
        return self.internal_stack.peep()


def problem1() -> Stack:
    """How would you design a stack which, in addition to push and pop, also has a min
    function which returns the minimum element? Push, pop, and min should all operate on O(1) time"""
    st = StackWithMin()
    st.push(2)
    st.push(4)
    st.push(1)
    st.push(6)
    print(st.peep())
    print(f'm: {st.min()}')
    print(st.pop())
    print(st.pop())
    print(f'm: {st.min()}')
    print(st.peep())
    return st


class SetOfStacks:
    def __init__(self, maximum):
        self.current_length = 0
        self.maximum = maximum
        self.stacks = [Stack()]

    def push(self, data):
        if self.current_length == self.maximum:
            print('adding stack!')
            self.current_length = 0
            self.stacks.append(Stack())
        else:
            self.current_length += 1
        self.current_stack().push(data)

    def pop(self):
        popped = self.current_stack().pop()
        if self.current_length == 0:
            print('removing stack!')
            self.stacks.pop()
            self.current_length = self.maximum
        else:
            self.current_length -= 1

        return popped

    def peep(self):
        return self.current_stack().peep()

    def current_stack(self):
        return self.stacks[-1]

    def popAt(self, substack):
        stack = self.stacks[substack]
        popped = stack.pop()
        for i in range(substack, len(self.stacks) - 1):
            cur_stack = self.stacks[i]
            next_stack = self.stacks[i+1]
            front = next_stack.popFront()
            print(f'front: {front}')
            cur_stack.push(front)
        if self.current_length == 0:
            print("shouldnt be here")
            self.stacks.pop()
            self.current_length = self.maximum
        self.current_length -= 1

        return popped

def problem2():
    """Implement a data structure SetOfStacks that is composed of several stacks and should
    create a new stack once the previosu one exceeds capacity."""
    sos = SetOfStacks(2)
    sos.push(2)
    print(f'peep: {sos.peep()}')
    sos.push(4)
    print(f'peep: {sos.peep()}')
    sos.push(6)
    print(f'peep: {sos.peep()}')
    sos.push(8)
    print(f'peep: {sos.peep()}')
    print(f'special: {sos.popAt(0)}')
    print(f'p: {sos.pop()}')
    print(f'p: {sos.pop()}')
    print(f'p: {sos.pop()}')


class TowerOfHanoi:
    def __init__(self, depth):
        self.depth = depth
        self.stacks = {
            'left': Stack(),
            'mid': Stack(),
            'right': Stack()
        }
        for i in reversed(range(depth)):
            self.stacks['left'].push(i + 1)

    def find_stack(self, n):
        for stack in self.stacks.values():
            if stack.peep() == n:
                return stack

    def get_dir_from_stack(self, match):
        for dir, stack in self.stacks.items():
            if stack == match:
                return dir

    def print_stacks(self):
        print('----------------------------')
        for t, stack in self.stacks.items():
            prepend = f'{t} stack:'
            stack.print_all(prepend)
        print('----------------------------')

    def solve_tower(self, depth, source, buffer, destination):
        dir1, dir2, dir3 = self.get_dir_from_stack(source), self.get_dir_from_stack(buffer), self.get_dir_from_stack(destination)
        print(f'solver! depth: {depth}, source = {dir1}, buffer = {dir2}, dest = {dir3}')

        if not depth:
            return
        if depth == 1:
            destination.push(source.pop())
            return

        self.solve_tower(depth-1, source, destination, buffer)
        self.print_stacks()

        destination.push(source.pop())
        self.print_stacks()

        self.solve_tower(depth-1, buffer, source, destination)
        self.print_stacks()

    def visualize_tower(self):
        list_of_values = []
        for stack in self.stacks.values():
            vals = []
            while stack.peep():
                vals.append(stack.pop())
            reversed(vals)

            list_of_values.append(vals)

        index = 0
        for stack in self.stacks.values():
            cur_list = list_of_values[index]
            for item in cur_list:
                stack.push(item)
            index += 1

        for l in list_of_values:
            for i in range(self.depth - len(l)):
                l.append('|')

        for i in range(len(list_of_values)):
            list_of_values[i] = list(reversed(list_of_values[i]))

        columns = []
        for i in range(self.depth):
            columns.append([])

        for l in list_of_values:
            for i in reversed(range(len(l))):
                columns[i].append(str(l[i]))

        for col in columns:
            print(' '.join(col))
        print("_ _ _")

        return list_of_values


def problem3(n: int):
    """towers of hanoi"""

    towers = TowerOfHanoi(n)
    towers.print_stacks()
    towers.solve_tower(n, towers.stacks['left'], towers.stacks['mid'], towers.stacks['right'])


class MyQueue:
    def __init__(self):
        self.older = Stack()
        self.newer = Stack()
        self.length = 0

    def enqueue(self, data):
        if self.older.peep():
            popped = self.older.pop()
            while popped:
                self.newer.push(popped)
                popped = self.older.pop()
        self.length += 1

        self.newer.push(data)

    def dequeue(self):
        popped = self.newer.pop()
        while popped:
            self.older.push(popped)
            popped = self.newer.pop()
        self.length -= 1
        return self.older.pop()

    def peek(self):
        popped = self.newer.pop()
        while popped:
            self.older.push(popped)
            popped = self.newer.pop()
        return self.older.peep()

    def empty(self):
        return not self.length


def problem4():
    """Implement a MyQueue class which implements a queue using two stacks"""
    q = MyQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue())
    print(q.dequeue())
    q.enqueue(11)
    q.enqueue(12)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())


def problem5():
    """Write a program to sort a stack in ascending order (with biggest items on top). You may
    use at most one additional stack to hold items, but you may not copy the elements into any
    other data structure. The stack supports push, pop, peek, and isEmpty()"""
    stack = Stack()
    stack.push(8)
    stack.push(1)
    stack.push(6)
    stack.push(3)
    stack.push(4)
    stack.push(2)
    stack.push(5)

    sorted_stack = Stack()

    while not stack.isEmpty():
        stack.print_all('starting: ')
        sorted_stack.print_all('sorted: ')

        value_to_sort = stack.pop()
        print(f'value to sort: {value_to_sort}')
        if sorted_stack.isEmpty():
            sorted_stack.push(value_to_sort)
        else:
            while not sorted_stack.isEmpty():
                if value_to_sort < sorted_stack.peep():
                    print('here')
                    sorted_stack.push(value_to_sort)
                    break
                else:
                    stack.push(sorted_stack.pop())
    return sorted_stack


class Animal:
    def __init__(self, name):
        self.time_created = datetime.now()
        self.name = name

    def is_older(self, other: 'Animal'):
        return self.time_created < other.time_created


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.name = name

    def get_name(self):
        return self.name


class AnimalQueue:
    def __init__(self):
        self.cat_queue = MyQueue()
        self.dog_queue = MyQueue()
        self.oldest_cat = None
        self.oldest_dog = None

    def isEmpty(self):
        return self.dog_queue.empty() and self.cat_queue.empty()

    def enqueue(self, animal: Animal):
        if isinstance(animal, Cat):
            self.cat_queue.enqueue(animal)
        else:
            self.dog_queue.enqueue(animal)

    def dequeue_dog(self):
        if self.dog_queue.empty():
            return None
        return self.dog_queue.dequeue()

    def dequeue_cat(self):
        if self.cat_queue.empty():
            return None
        return self.cat_queue.dequeue()

    def dequeue_any(self):
        dog = self.dog_queue.peek()
        cat = self.cat_queue.peek()
        if not dog or cat.is_older(dog):
            return self.dequeue_cat()
        if not cat or dog.is_older(cat):
            return self.dequeue_dog()

def problem6():
    """An animal shelter holds only dogs and cats, and operations on a strictly first in first out
    basis. People can select where they want a cat or a dog, or have no preference. Create a data
    structure to maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog, dequeueCat"""

    q = AnimalQueue()
    q.enqueue(Dog('Fritz'))
    q.enqueue(Cat('Frida'))
    q.enqueue(Cat('Diego'))
    q.enqueue(Dog('Frankie'))



    print(q.dequeue_cat().name)
    print(q.dequeue_cat().name)
    print(q.dequeue_dog().name)
    print(q.dequeue_dog().name)
    q.enqueue(Dog('Chorizo'))
    q.enqueue(Cat('Kahlo'))
    print(q.dequeue_any().name)
    print(q.dequeue_any().name)


if __name__ == "__main__":
    problem1()
    problem2()
    problem3(5)
    problem4()
    problem5()
    problem6()



