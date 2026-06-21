from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    parents = deque([root])
    index = 1

    while parents and index < len(values):
        parent = parents.popleft()

        if values[index] is not None:
            parent.left = TreeNode(values[index])
            parents.append(parent.left)
        index += 1

        if index < len(values) and values[index] is not None:
            parent.right = TreeNode(values[index])
            parents.append(parent.right)
        index += 1

    return root
