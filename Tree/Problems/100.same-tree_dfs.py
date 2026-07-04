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

        self.is_same = True

        if p is None and q is None:
            return True
        
        if p is not None and q is None or p is None and q is not None :  
            return False   
        
        self.dfs(p,q)

        return self.is_same
    
    def dfs(self, p,q):

        if p.val != q.val:
            self.is_same = False
            return False
        
        if p.left is None and q.left is None and p.right is None and q.right is None:
            return True
    
        if p.left is not None and q.left is None or p.left is None and q.left is not None :  
            self.is_same = False
            return False   
            
        if p.right is not None and q.right is None or  p.right is None and q.right is not None :  
            self.is_same = False
            return False
        
        
        
        is_left_tree_same = True
        is_right_tree_same = True
        if p.left and q.left:
            is_left_tree_same = self.dfs(p.left, q.left)

        if p.right and q.right:
            is_right_tree_same = self.dfs(p.right, q.right)

        if is_left_tree_same and is_right_tree_same:
            return True
        else:
            self.is_same = False
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
"""