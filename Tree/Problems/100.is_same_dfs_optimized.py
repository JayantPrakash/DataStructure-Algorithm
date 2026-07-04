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

        if not p and not q:
            return True
        
        if p and q and p.val==q.val:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right, q.right) 
        else:
            return False

sol = Solution()
p = [1,2,3]
p = [1,2]
q = [1,None,2]
rootp = build_tree(p)
#q = [1,2,3]
rootq = build_tree(q) 

print(sol.isSameTree(rootp, rootq))                  

"""
Logic:
Time and space complexity
T(n) = O(n)
S(n) = O(n)

Pattern - DFS    

1. if p is none and q is none : True
2. if p and q and p.val != q.val: return self.isSameTree(p.left,q.left) and self.isSameTree(p.right, q.right) 
   else:
   return False
"""           