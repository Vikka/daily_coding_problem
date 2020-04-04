"""
A unival tree (which stands for "universal value") is a tree where all nodes
under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

       0
      / \
     1   0
        / \
       1   0
      / \
     1   1
"""
from typing import Union, Optional


class Node:
    def __init__(self, value: int,
                 left: Optional = None,
                 right: Optional = None):
        self.value = value
        self.left: Optional[Node] = left
        self.right: Optional[Node] = right

    def __str__(self):
        return f'value: {self.value}, left<{self.left}>, right<{self.right}>'


def count_unival_subtree(node: Node) -> int:
    if not (node.left is None or node.right is None):
        res = count_unival_subtree(node.left) \
               + count_unival_subtree(node.right) \
               + int(node.left.value == node.right.value)
        return res

    if node.left is not None:
        res = count_unival_subtree(node.left)
        return res

    if node.right is not None:
        res = count_unival_subtree(node.right)
        return res

    else:
        return 1


if __name__ == '__main__':
    foo = Node(0,
               Node(1),
               Node(0,
                    Node(1,
                         Node(1),
                         Node(1)),
                    Node(0)))
    assert count_unival_subtree(foo) == 5
