"""
Given the root to a binary tree, implement serialize(root), which serializes
the tree into a string, and deserialize(s), which deserializes the string back
into the tree.

For example, given the following Node class

    class Node:
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

The following test should pass:

    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'
"""
from typing import Optional


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(node: Node) -> Optional[str]:
    # format: root(<Node>, <Node>)
    if not node:
        return None
    if not (node.left or node.right):
        return f'{node.val}'
    serialized_root = f'{node.val if node else None}(' \
                      f'{serialize(node.left)}, ' \
                      f'{serialize(node.right)})'
    return serialized_root


def find_arg_start(node: str) -> Optional[int]:
    first_parenthesis = node.find('(')
    first_comma = node.find(',')
    lowest = list()
    if first_parenthesis != -1:
        lowest.append(first_parenthesis)
    if first_comma != -1:
        lowest.append(first_comma)
    if lowest:
        return min(lowest)
    return None


def find_next_comma(node_args: str) -> Optional[int]:
    parenthesis_count = int()
    for i, c in enumerate(node_args):
        if c == '(':
            parenthesis_count += 1
        elif c == ')':
            parenthesis_count -= 1
        elif c == ',' and not parenthesis_count:
            return i
    return None


def deserialize(node: str) -> Node:
    # root(left(left.left, None),right)
    arg_start = find_arg_start(node)

    if not arg_start:
        return Node(node) if node != 'None' else None

    name = node[:arg_start]
    comma_i = arg_start + find_next_comma(node[arg_start + 1: -1]) + 1
    if comma_i:
        left = deserialize(node[arg_start + 1:comma_i])
        right = deserialize(node[comma_i + 2:-1])
        return Node(name, left, right)
    return Node(name)


if __name__ == '__main__':
    root = Node('root', Node('left', Node('left.left')), Node('right'))
    print(serialize(root))
    print(deserialize(serialize(root)))
    deserialize_node = deserialize(serialize(root))
    print(serialize(deserialize(serialize(root))))
    assert deserialize(serialize(root)).left.left.val == 'left.left'
