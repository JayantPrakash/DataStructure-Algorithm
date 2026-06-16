from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.global_dia = 0

        self.dfs(root)

        return self.global_dia
    
    def dfs(self, node):

        if node.left is None and node.right is None:
            return 0
        
        local_dia = 0
        left_dia = 0
        right_dia = 0

        if node.left is not None:
            left_dia = self.dfs(node.left)
            local_dia = left_dia + 1

        if node.right is not None:
            right_dia = self.dfs(node.right)
            local_dia += right_dia + 1

        if self.global_dia < local_dia:
            self.global_dia = local_dia

        return max(left_dia, right_dia) + 1


            

