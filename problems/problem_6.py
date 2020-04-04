"""" An XOR linked list is a more memory efficient doubly linked list.
Instead of each node holding next and prev fields, it holds a field named
both, which is a XOR of the next node and the previous node. Implement a XOR
linked list; it has an add(element) which adds the element to the end,
and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you
have access to 'get_pointer' and 'dereference_pointer' functions that
converts between nodes and memory addresses. """
from typing import Any


def get_pointer(element) -> int:
    ...


def dereference_pointer(pointer: int) -> Any:
    ...


class Node:
    both: int

    def add(self, element, previous: int = None):
        if not self.both:
            self.both = get_pointer(element)
        elif not previous:
            next_node: Node = dereference_pointer(self.both)
            next_node.add(element, get_pointer(self))
        else:
            next_node: Node = dereference_pointer(self.both ^ previous)
            next_node.add(element, get_pointer(self))

    def get(self, index, previous: int = None, current: int = 0):
        if index == current:
            return self
        if not previous:
            dereference_pointer(self.both).get(index, self, current + 1)
        else:
            dereference_pointer(self.both ^ previous)\
                .get(index, self, current + 1)


if __name__ == '__main__':
    ...