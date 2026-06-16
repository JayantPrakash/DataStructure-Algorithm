from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        self.isBalanced = True
        self.dfs(root)
        return self.isBalanced
    
    def dfs(self, node):

        if node.left is None and node.right is None:
            return 1
        
        left_depth = 0
        right_depth = 0

        if node.left is not None:
            left_depth = self.dfs(node.left)

        if node.right is not None:
            right_depth = self.dfs(node.right)

        if abs(left_depth - right_depth) > 1:
            self.isBalanced = False

        return max(left_depth, right_depth) + 1


            
"""
Make sure to have the depth of leaf node to be 1,
otherwise only node with right subtree will give wrong result
ex: [1,null,2,null,3]

"""
