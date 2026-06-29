"""
Question:
Given the roots of two binary trees p and q, write a function to 
check if they are the same or not.
Two binary trees are considered the same if they 
are structurally identical, and the nodes have the same value.
"""

# Definition for a binary tree node.
from collections import deque

from build_tree import build_tree
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """

        queue = deque([(p,q)])

        if p is None and q is None:
            return True

        if p is None and q is not None or p is not None and q is None:
            return False
    

        while len(queue) != 0:
            nodep, nodeq = queue.popleft()
            
            if nodep.val != nodeq.val:
                return False

            if nodep.left is not None and nodeq.left is None or  nodep.left is None and nodeq.left is not None :  
                return False   
            
            if nodep.right is not None and nodeq.right is None or  nodep.right is None and nodeq.right is not None :  
                return False
                     
            
            if nodep.left and nodeq.left:
                queue.append((nodep.left, nodeq.left))

            if nodep.right and nodeq.right:
                queue.append((nodep.right, nodeq.right))
        
        return True      


sol = Solution()
p = [1,2,3]
rootp = build_tree(p)
q = [1,2,3]
rootq = build_tree(q) 

print(sol.isSameTree(rootp, rootq))                  

"""
Logic:
Time and space complexity
T(n) = O(n)
S(n) = O(n)

Pattern - BFS    

1. Check boundary condition when [] and [1] is there
if (p is None and q is not None) or (p is not None and q is None):
            return False
2. Create deque and add root of each tree to queue.
qu = deque([(p,q)])
3. check value is same for each tree
    if node_p.val != node_q.val:
            return False
4. Check if the structure is same
    if (node_p.left is not None and node_q.left is None) or (node_p.left is None and node_q.left is not None):
        return False
    if (node_p.right is not None and node_q.right is None) or (node_p.right is None and node_q.right is not None):
        return False
5. Check if both left and right node of each tree is not None: append to the queue
   qu.append((node_p.left, node_q.left)) and qu.append((node_p.right, node_q.right))            
"""