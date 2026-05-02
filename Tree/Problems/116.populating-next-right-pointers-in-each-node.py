from typing import Optional
from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return []
        
        q = deque()
        q.append(root)

        while len(q) != 0:
            num_nodes = len(q)

            for i in range(len(q)):
                node = q.popleft()

                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:    
                    q.append(node.right)

                #first node of level, only capture prev
                if i == 0:
                    prev_node = node
                # non first level of each node, connect prev next to the current node
                else:
                    prev_node.next = node
                    prev_node = node

            # make next of last node of level to None 
            prev_node = None
        return root

sol = Solution()
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)     

print(sol.connect(root))                            

"""
Time and space complexity
T(n) = O(n)
S(n) = O(n)

Pattern - BFS    
Note: if it is the first node in the level, just capture prev node only,
otherwsise make the prevnode next to the current node and prev node to the current node
At the end of level, make prev node next equivalent to None
        if i == 0:
            prev_node = node
        else:
            prev_node.next = node
            prev_node = node

prev_node = None
"""        