from typing import Optional

from sqlalchemy import null
from build_tree import build_tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':  
        self.p_ancs = [] 
        self.q_ancs = []
        self.p = p
        self.q = q 
        self.dfs(root, [])

        self.p_ancs = self.p_ancs[0]
        self.q_ancs = self.q_ancs[0]
        common_ancs = []    
        for i in range(len(self.p_ancs)):
            for j in range(len(self.q_ancs)):
                if self.p_ancs[i].val == self.q_ancs[j].val:
                    common_ancs.append(self.p_ancs[i])
        return common_ancs[-1]

    def dfs(self, node, slate):

        slate.append(node)

        if node.val == self.p.val:
            self.p_ancs.append(slate[:])

        if node.val == self.q.val:
            self.q_ancs.append(slate[:])

        if node.left is not None:
            self.dfs(node.left, slate)

        if node.right is not None:
            self.dfs(node.right, slate)
        
        slate.pop()


sol = Solution()
list_val = [1,2]
root = build_tree(list_val)
 
print(sol.lowestCommonAncestor(root,TreeNode(1), TreeNode(2)))                  
