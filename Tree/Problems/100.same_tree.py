# Definition for a binary tree node.
from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        q1 = deque()
        q1.append((p,1))
        len_q1 = len(q1)

        q2 = deque()
        q2.append((q,1))


        while len(q1) != 0:
            num_nodes_p = len(q1)

            for _ in range(num_nodes_p):
                node_p, id_p = q1.popleft()
                node_q, id_q = q2.popleft()

                if node_p != node_q or id_p != id_q:
                    return False

                if node_p.left is not None:
                    q1.append((node_p.left, 2*id_p))

                if node_p.right is not None:
                    q1.append((node_p.right, 2*id_p + 1))

                if node_q.left is not None:
                    q2.append((node_q.left, 2*id_q))

                if node_q.right is not None:
                    q2.append((node_q.right, 2*id_q + 1))
        
        return True       
                        

"""
Time and space complexity
T(n) = O(n)
S(n) = O(n)

Pattern - BFS    
"""