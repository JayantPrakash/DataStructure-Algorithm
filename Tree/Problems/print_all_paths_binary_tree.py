# Definition for a binary tree node.
from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def print_all_paths(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None:
            return []
        
        self.result = []

        self.dfs(root, [])
        return self.result

    def dfs(self, node, slate):

        slate.append(node.val)

        if node.left is None and node.right is None:
            self.result.append(slate[:])

        if node.left is not None:
            self.dfs(node.left, slate)  

        if node.right is not None:
            self.dfs(node.right, slate)       

        slate.pop()           
    

sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)     

print(sol.print_all_paths(root))       