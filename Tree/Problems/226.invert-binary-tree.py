from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root is None:
            return None
        
        self.root = root
        self.dfs(self.root)
        return self.root


    def dfs(self,node):

        if node.left is not None:
            self.dfs(node.left)

        if node.right is not None:
            self.dfs(node.right)

        temp_node = node.left
        node.left = node.right
        node.right = temp_node        