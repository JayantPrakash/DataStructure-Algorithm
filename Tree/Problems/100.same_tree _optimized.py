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
        
        if (p is None and q is not None) or (p is not None and q is None):
            return False
        
        qu = deque([(p,q)])

        while len(qu) != 0:
            num_nodes = len(qu)

            for _ in range(num_nodes):
                node_p, node_q = qu.popleft()

                if node_p.left is not None and node_q.left is not None:
                    qu.append((node_p.left, node_q.left))
                
                if node_p.right is not None and node_q.right is not None:
                    qu.append((node_p.right, node_q.right))

                # check structure is same for both tree
                if (node_p.left is not None and node_q.left is None) or (node_p.left is None and node_q.left is not None):
                    return False
                if (node_p.right is not None and node_q.right is None) or (node_p.right is None and node_q.right is not None):
                    return False

                # check value is same for each tree
                if node_p.val != node_q.val:
                     return False
        
        return True       
                        

"""
Time and space complexity
T(n) = O(n)
S(n) = O(n)

Pattern - BFS    

1. Check boundary condition when [] and [1] is there
if (p is None and q is not None) or (p is not None and q is None):
            return False
2. Create deque and add root of each tree to queue.
qu = deque([(p,q)])
3. Check if both left and right node of each tree is not None: append to the queue
qu.append((node_p.left, node_q.left)) and qu.append((node_p.right, node_q.right))
4. Check if the structure is same
    if (node_p.left is not None and node_q.left is None) or (node_p.left is None and node_q.left is not None):
        return False
    if (node_p.right is not None and node_q.right is None) or (node_p.right is None and node_q.right is not None):
        return False

5. check value is same for each tree
    if node_p.val != node_q.val:
            return False
"""