# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.postOrderHelper(root, result)
        return result
    
    def postOrderHelper(self,node, res):

        if not node:
            return None
        
        self.postOrderHelper(node.left, res)
        self.postOrderHelper(node.right, res)
        res.append(node.val)

sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)     

print(sol.postorderTraversal(root))        