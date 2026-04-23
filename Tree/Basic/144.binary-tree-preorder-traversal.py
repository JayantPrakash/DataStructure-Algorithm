# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.preorderHelper(root, result)
        return result
    
    def preorderHelper(self, node, res):
        if not node:
            return None
        
        res.append(node.val)
        self.preorderHelper(node.left, res)
        self.preorderHelper(node.right, res)

sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)     

print(sol.preorderTraversal(root))

# Time and space complexity
# T(n) = O(n)
# S(n) = O(n)


        
