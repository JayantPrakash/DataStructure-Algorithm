# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.inOrderHelper(root, result)
        return result
    
    def inOrderHelper(self,node, res):

        if not node:
            return None
        
        self.inOrderHelper(node.left, res)
        res.append(node.val)
        self.inOrderHelper(node.right, res)

sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)     

print(sol.inorderTraversal(root))        