# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def dfs(self, root: Optional[TreeNode]) -> List[int]:

        result = []
        self.dfs_helper(root, result)

        return result
    
    def dfs_helper(self, node, res):

        if node is None:
            return None
        
        if node.left is not None:
            self.dfs_helper(node.left, res)
        if node.right is not None:
            self.dfs_helper(node.right, res)

        res.append(node.val)

sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)     

print(sol.dfs(root))


