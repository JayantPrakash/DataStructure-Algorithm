# Definition for a binary tree node.
from typing import List, Optional
from collections import deque
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        result = []
        if root is None:
            return result
        q = deque()
        q.append(root)
        len_q = len(q)

        while len(q) != 0:
            len_q = len(q)
            temp = []

            for _ in range(len_q):
                node = q.popleft
                temp.append(node)

                for child in node.children:
                    q.append(child)

            result.append(temp)
        return result            
    

"""
Time and space complexity
T(n) = O(n)
S(n) = O(n)

Pattern - BFS    
"""